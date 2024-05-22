from typing import List
from fastapi import APIRouter
from .function import get_insureds
from .model import Insured

router = APIRouter()

@router.get("/insureds", response_model=List[Insured])
async def get():
    return get_insureds()
