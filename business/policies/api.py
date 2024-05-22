from typing import List
from fastapi import APIRouter
from .function import get_policies
from .model import Policy

router = APIRouter()

@router.get("/policies", response_model=List[Policy])
async def get():
    return get_policies()
