from models import City, City_Pydantic, CityIn_Pydantic


async def get_cities():
    return await City_Pydantic.from_queryset(City.all())

async def get_cities_via_id(city_id : int):
    return await City_Pydantic.from_queryset_single(City.get(id = city_id))


async def create_city(city : CityIn_Pydantic):
    city_obj = await City.create(**city.dict(exclude_unset = True))
    return await City_Pydantic.from_tortoise_orm(city_obj)

async def delete_city(city_id : id):
    await City.filter(id = city_id).delete()
    return await "City deleted successfully"