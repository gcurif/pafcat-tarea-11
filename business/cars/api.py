from typing import List
from fastapi import APIRouter
from .function import get_cars
from .model import Car

router = APIRouter()

@router.get("/cars", response_model=List[Car])
async def get():
    return get_cars()
