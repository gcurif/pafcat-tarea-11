from typing import List
from fastapi import APIRouter
from .function import get_car_models

router = APIRouter()

@router.get("/car_models")
async def get():
    return get_car_models()
