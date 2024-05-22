from typing import List
from fastapi import APIRouter
from .function import get_car_models
from .model import CarModel

router = APIRouter()

@router.get("/car_models", response_model=List[CarModel])
async def get():
    return get_car_models()
