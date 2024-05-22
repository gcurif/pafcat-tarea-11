from typing import List
from fastapi import APIRouter
from .function import get_policies

router = APIRouter()

@router.get("/policies")
async def get():
    return get_policies()
