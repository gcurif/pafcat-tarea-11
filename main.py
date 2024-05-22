from fastapi import FastAPI
from business.car_brands.api import router as car_brands_router 

app = FastAPI()

app.include_router(car_brands_router)
