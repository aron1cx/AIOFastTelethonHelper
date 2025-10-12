"""
`AIOFastTelethonHelper` — an fully asynchronous version of `FastTelethonHelper`.
Provides fast parallel file upload and download functions without blocking the event loop.

Based on `FastTelethonhelper` by original author `MiyukiKun`.
Modified and maintained by `Aron1cX`.
"""

from .core import fast_download, fast_upload

__all__ = ["fast_download", "fast_upload"]
