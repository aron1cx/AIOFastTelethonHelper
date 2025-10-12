from aiofiles.threadpool.binary import AsyncBufferedReader


async def read_buffer_chunks(buffer: AsyncBufferedReader, chunk_size: int = 1024):
    while True:
        chunk = await buffer.read(chunk_size)
        if not chunk:
            break

        yield chunk


def human_readable_size(size, decimal_places=2):
    for unit in ["B", "KB", "MB", "GB", "TB", "PB"]:
        if size < 1024.0 or unit == "PB":
            break

        size /= 1024.0

    return f"{round(size, decimal_places)}{unit}"

