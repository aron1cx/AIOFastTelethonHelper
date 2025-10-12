from typing import Union
from telethon.tl.types import (
    InputPeerPhotoFileLocation,
    InputDocumentFileLocation,
    InputPhotoFileLocation,
    InputFileLocation,
    Document,
)


TypeLocation = Union[
    InputPeerPhotoFileLocation,
    InputDocumentFileLocation,
    InputPhotoFileLocation,
    InputFileLocation,
    Document,
]
