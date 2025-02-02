# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Any, Dict

from pydantic import BaseModel, Extra


class Key(BaseModel):
    class Config:
        extra = Extra.forbid

    address: str
    nat: str


class SplitSignStorageItem(BaseModel):
    class Config:
        extra = Extra.forbid

    key: Key
    value: Dict[str, Any]


class SplitSignStorage(BaseModel):
    __root__: List[SplitSignStorageItem]
