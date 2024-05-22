from typing import List
from fastapi import APIRouter
from .function import get_car_brands

router = APIRouter()

@router.get("/car_brands")
async def get():
    return get_car_brands()
