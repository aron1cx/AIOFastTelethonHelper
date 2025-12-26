import hashlib
import inspect
import logging
import os
import time
from typing import Callable, Optional

from aiofiles.threadpool.binary import AsyncBufferedIOBase, AsyncBufferedReader
from telethon import TelegramClient
from telethon.helpers import generate_random_long
from telethon.tl.types import (
    InputFile,
    InputFileBig,
    TypeInputFile,
)
from telethon.utils import get_input_location

from .transfer import ParallelTransferrer
from .types import TypeLocation
from .util import read_buffer_chunks

logger = logging.getLogger("AIOFastTelethonHelper")


async def download_file(
    client: TelegramClient,
    location: TypeLocation,
    out: AsyncBufferedIOBase,
    progress_callback: Optional[Callable] = None,
) -> AsyncBufferedIOBase:
    file_size = location.size
    dc_id, location = get_input_location(location)

    logger.info(f"Start download file: {location} ({file_size}B)")

    downloader = ParallelTransferrer(client, dc_id)
    downloaded = downloader.download(location, file_size)

    start_time = time.time()
    async for x in downloaded:
        await out.write(x)
        if progress_callback:
            done = await out.tell()
            func = progress_callback(done=done, total=file_size, start_time=start_time)

            if inspect.isawaitable(func):
                try:
                    await func
                except BaseException:
                    pass

    return out


async def download_file_stream(
    client: TelegramClient,
    location: TypeLocation,
):
    file_size = location.size
    dc_id, input_location = get_input_location(location)

    downloader = ParallelTransferrer(client, dc_id)
    downloaded = downloader.download(input_location, file_size)

    async for chunk in downloaded:
        yield chunk


async def upload_file(
    client: TelegramClient,
    reader: AsyncBufferedReader,
    file_name: str,
    progress_callback: Optional[Callable] = None,
) -> TypeInputFile:
    file_size = os.path.getsize(reader.name)
    file_id = generate_random_long()

    hash_md5 = hashlib.md5()
    uploader = ParallelTransferrer(client)
    part_size, part_count, is_large = await uploader.init_upload(file_id, file_size)

    buffer = bytearray()
    start_time = time.time()
    async for data in read_buffer_chunks(reader):
        if progress_callback:
            done = await reader.tell()
            func = progress_callback(done=done, total=file_size, start_time=start_time)
            if inspect.isawaitable(func):
                try:
                    await func
                except BaseException:
                    pass

        if not is_large:
            hash_md5.update(data)

        if len(buffer) == 0 and len(data) == part_size:
            await uploader.upload(data)
            continue

        new_len = len(buffer) + len(data)
        if new_len >= part_size:
            cutoff = part_size - len(buffer)
            buffer.extend(data[:cutoff])
            await uploader.upload(bytes(buffer))
            buffer.clear()
            buffer.extend(data[cutoff:])
        else:
            buffer.extend(data)

    if len(buffer) > 0:
        await uploader.upload(bytes(buffer))

    await uploader.finish_upload()

    if is_large:
        return InputFileBig(file_id, part_count, file_name)
    else:
        return InputFile(file_id, part_count, file_name, hash_md5.hexdigest())
