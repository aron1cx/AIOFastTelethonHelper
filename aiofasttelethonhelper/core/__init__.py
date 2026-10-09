from __future__ import annotations

import os
from typing import Any, Callable

import aiofiles
from telethon import TelegramClient
from telethon.types import Message

from .methods import download_file, upload_file
from .path import resolve_download_path


async def fast_download(
    client: TelegramClient,
    message: Message,
    file_path: str | None = "./downloads",
    file_name: str | None = None,
    progress_callback: Callable[..., Any] | None = None,
) -> str:
    media = getattr(message, "document", None) or getattr(message, "media", None)
    file_obj = getattr(message, "file", None)
    if media is None and file_obj is None:
        raise ValueError("Message has no file to download")

    name = (
        file_name
        or getattr(file_obj, "name", None)
        or getattr(media, "name", None)
        or getattr(media, "title", None)
        or "unknown.bin"
    )

    final_path = resolve_download_path(file_path, file_name=name)

    location = media or file_obj
    if location is None:
        raise ValueError("Message has no file to download")

    async with aiofiles.open(final_path, "wb") as out:
        await download_file(
            client=client,
            location=location,  # type: ignore[arg-type]
            out=out,
            progress_callback=progress_callback,
        )

    return str(final_path)


async def fast_upload(
    client: TelegramClient,
    file_path: str,
    file_name: str | None = None,
    progress_callback: Callable[..., Any] | None = None,
) -> Any:
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
