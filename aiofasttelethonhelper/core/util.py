from __future__ import annotations

from collections.abc import AsyncGenerator

from aiofiles.threadpool.binary import AsyncBufferedReader


async def read_buffer_chunks(
    buffer: AsyncBufferedReader, chunk_size: int = 1024
) -> AsyncGenerator[bytes, None]:
    while True:
        chunk = await buffer.read(chunk_size)  # type: ignore[union-attr, attr-defined]
        if not chunk:
            break

        yield chunk


def human_readable_size(size: float, decimal_places: int = 2) -> str:
    unit = "B"
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size < 1024.0 or unit == "PB":
            break

        size /= 1024.0

    return f"{round(size, decimal_places)}{unit}"
