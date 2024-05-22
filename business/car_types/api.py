from typing import List
from fastapi import APIRouter
from .function import get_car_types
from .model import CarType

router = APIRouter()

@router.get("/car_types", response_model=List[CarType])
async def get():
    return get_car_types()
