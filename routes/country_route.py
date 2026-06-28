from fastapi import APIRouter
from repository import country_repo
from models import CountryIn_Pydantic

router = APIRouter(
    tags=["Countries"],
    prefix="/countries"
)

@router.get("/")
async def get_countries():
    return await country_repo.get_countries()


@router.get("/{country_id}")
async def get_country_via_id(country_id : int):
    return await country_repo.get_countries_via_id(country_id)


@router.post("/")
async def create_country(country : CountryIn_Pydantic):
    return await country_repo.create_countries(country)


@router.delete("/{country_id}")
async def remove_country(country_id : int):
    return await country_repo.delete_country(country_id)


