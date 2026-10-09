from __future__ import annotations

from telethon.tl.types import (
    Document,
    InputDocumentFileLocation,
    InputFileLocation,
    InputPeerPhotoFileLocation,
    InputPhotoFileLocation,
)

TypeLocation = (
    InputPeerPhotoFileLocation
    | InputDocumentFileLocation
    | InputPhotoFileLocation
    | InputFileLocation
    | Document
)
