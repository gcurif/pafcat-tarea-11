from typing import List
from fastapi import APIRouter
from .function import get_claims
from .model import Claim

router = APIRouter()

@router.get("/claims", response_model=List[Claim])
async def get():
    return get_claims()
