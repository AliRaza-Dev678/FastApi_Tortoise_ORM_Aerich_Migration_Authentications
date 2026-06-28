from models import Users, Users_Pydantic, UsersIn_Pydantic

async def login(user : UsersIn_Pydantic):
    user_obj = await Users.create(**user.dict(exclude_unset = True))
    return Users_Pydantic.from_tortoise_orm(user_obj)
