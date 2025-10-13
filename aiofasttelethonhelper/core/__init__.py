from telethon import TelegramClient
from telethon.types import Message

from .methods import download_file, upload_file
from typing import Optional, Callable

import aiofiles, os


async def fast_download(
    client: TelegramClient,
    message: Message,
    file_path: Optional[str] = "./downloads",
    file_name: Optional[str] = None,
    progress_callback: Optional[Callable] = None,
):
    if os.path.splitext(file_path)[1]:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
    else:
        file_path = os.path.join(file_path, file_name or message.file.name or "unknown.bin")
        os.makedirs(file_path, exist_ok=True)

    async with aiofiles.open(file_path, "wb") as out:
        await download_file(
            client=client,
            location=message.document,
            out=out,
            progress_callback=progress_callback,
        )

    return file_path


async def fast_upload(
    client: TelegramClient,
    file_path: str,
    file_name: Optional[str] = None,
    progress_callback: Optional[Callable] = None,
):
    if file_name is None:
        file_name = os.path.basename(file_path)

    async with aiofiles.open(file_path, "rb") as reader:
        file = await upload_file(
            client=client,
            reader=reader,
            file_name=file_name,
            progress_callback=progress_callback,
        )

    return file
