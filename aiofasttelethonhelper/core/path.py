from __future__ import annotations

import os
from pathlib import Path


def resolve_download_path(
    file_path: str | Path | None,
    file_name: str | None = None,
    *,
    fallback_name: str = "unknown.bin",
) -> Path:
    final_path = Path(file_path) if file_path is not None else Path("./downloads")

    name = file_name or fallback_name

    if final_path.is_dir() or str(final_path).endswith(("/", os.sep)):
        final_path = final_path / name
        final_path.parent.mkdir(parents=True, exist_ok=True)
        return final_path

    if not final_path.suffix and not final_path.exists():
        final_path = final_path / name

    final_path.parent.mkdir(parents=True, exist_ok=True)
    return final_path
