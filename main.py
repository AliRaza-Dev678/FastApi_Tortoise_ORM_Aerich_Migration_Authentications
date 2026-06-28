from fastapi import FastAPI
from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise.contrib.fastapi import register_tortoise
from config import TORTOISE_ORM
from routes import user_route, country_route, authentication_route, city_route

app = FastAPI()

app.include_router(city_route.router)
app.include_router(country_route.router)
app.include_router(authentication_route.router)
app.include_router(user_route.router)



register_tortoise(
    app,
    config=TORTOISE_ORM,
    # modules={"models" : ["models"]}, dont need to use this bcz this is defined in config.py
    generate_schemas=False,  # false bcz now aerich will handle this
    add_exception_handlers=True
)