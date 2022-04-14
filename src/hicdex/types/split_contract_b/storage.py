# generated by datamodel-codegen:
#   filename:  storage.json

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Extra


class SplitContractBStorage(BaseModel):
    class Config:
        extra = Extra.forbid

    administrator: str
    coreParticipants: List[str]
    isPaused: bool
    marketplaceAddress: str
    minterAddress: str
    proposedAdministrator: Optional[str]
    registryAddress: str
    residuals: Optional[str]
    shares: Dict[str, str]
    threshold: Optional[str]
    tokenAddress: str
    totalReceived: Optional[str]
    totalShares: str
    undistributed: Optional[Dict[str, str]]
