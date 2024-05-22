from typing import List
from fastapi import APIRouter
from .function import get_cars

router = APIRouter()

@router.get("/cars")
async def get():
    return get_cars()
