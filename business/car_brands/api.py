from typing import List
from fastapi import APIRouter
from .function import get_car_brands
from .model import CarBrand

router = APIRouter()

@router.get("/car_brands", response_model=List[CarBrand])
async def get():
    return get_car_brands()
