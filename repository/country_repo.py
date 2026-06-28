from models import Country, Country_Pydantic, CountryIn_Pydantic

async def get_countries():
    return await Country_Pydantic.from_queryset(Country.all())


async def get_countries_via_id(country_id : int):
    return await Country_Pydantic.from_queryset_single(Country.get(id = country_id))

async def create_countries(country : CountryIn_Pydantic):
    country_obj = await Country.create(**country.dict(exclude_unset = True))
    return await Country_Pydantic.from_tortoise_orm(country_obj)

async def delete_country(country_id : int):
    return await Country.filter(id = country_id).delete()


