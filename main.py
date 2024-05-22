from fastapi import FastAPI
from business.car_brands.api import router as car_brands_router
from business.car_models.api import router as car_models_router
from business.car_types.api import router as car_types_router
from business.cars.api import router as car_router
from business.claims.api import router as claim_router
from business.policies.api import router as policy_router

app = FastAPI()

app.include_router(car_brands_router)
app.include_router(car_models_router)
app.include_router(car_types_router)
app.include_router(car_router)
app.include_router(claim_router)
app.include_router(policy_router)