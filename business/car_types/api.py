from typing import List
from fastapi import APIRouter
from .function import get_car_types

router = APIRouter()

@router.get("/car_types")
async def get():
    return get_car_types()
