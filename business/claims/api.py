from typing import List
from fastapi import APIRouter
from .function import get_claims

router = APIRouter()

@router.get("/claims")
async def get():
    return get_claims()
