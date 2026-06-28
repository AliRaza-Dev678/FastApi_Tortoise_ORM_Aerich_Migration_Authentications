from fastapi import APIRouter
from repository import city_repo
from models import CityIn_Pydantic


router = APIRouter(
    tags=["Cities"],
    prefix="/cities"
)

@router.get("/")
async def get_cities():
    return await city_repo.get_cities()

@router.get("/{city_id}")
async def get_city_via_id(city_id : int):
    return await city_repo.get_cities_via_id(city_id)

@router.post("/")
async def create_city(city : CityIn_Pydantic):
    return await city_repo.create_city(city)

@router.delete("/{city_id}")
async def remove_city(city_id : int):
    return city_repo.delete_city(city_id)



