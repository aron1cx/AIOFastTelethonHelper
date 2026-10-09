from __future__ import annotations

from pathlib import Path

from aiofasttelethonhelper.core.path import resolve_download_path


def test_resolve_when_given_dir_ends_with_sep(tmp_path: Path) -> None:
    dest = tmp_path / "downloads" / ""
    dest.mkdir(parents=True, exist_ok=True)
    result = resolve_download_path(str(dest), file_name="file.txt")
    assert result == dest / "file.txt"


def test_resolve_when_given_dir_without_sep(tmp_path: Path) -> None:
    dest = tmp_path / "downloads"
    dest.mkdir()
    result = resolve_download_path(str(dest), file_name="file.txt")
    assert result == dest / "file.txt"


def test_resolve_when_given_full_path_with_extension(tmp_path: Path) -> None:
    dest = tmp_path / "downloads" / "file.txt"
    result = resolve_download_path(str(dest))
    assert result == dest
    assert dest.parent.exists()
