from typing import List
from fastapi import APIRouter
from .function import get_insureds

router = APIRouter()

@router.get("/insureds")
async def get():
    return get_insureds()
