from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class City(Model):
    id = fields.IntField(primary_key=True)
    name = fields.CharField(max_length = 255)
    timezone = fields.CharField(max_length = 255)

    def current_time(self) -> str:
        try:
            import pytz
            from datetime import datetime
            tz = pytz.timezone(self.timezone)
            return datetime.now(tz).isoformat()
        except Exception:
            return "Invalid timezone"
        


class Country(Model):
    id = fields.IntField(pk = True)
    name = fields.CharField(max_length=255)
    population = fields.IntField(default=0)

    def population_count(self) -> str:
        try:
            import requests
            r = requests.get(f"https://restcountries.com/v3.1/name/{self.name}")
            data = r.json()[0]
            population = data["population"]
            if population >= 1_000_000_000:
                return f"{population / 1_000_000_000:.2f} Billion"
            elif population >= 1_000_000:
                return f"{population / 1_000_000:.2f} Million"
            else:
                return f"{population / 1_000:.2f} Thousand"
        except Exception:
            return "Unknown"
    class PydanticMeta:              
        computed = ['population_count']   


class User(Model):
    id = fields.IntField(primary_key = True)
    name = fields.CharField(max_length = 255)
    email = fields.CharField(max_length = 255, unique = True)
    password = fields.CharField(max_length = 255)




City_Pydantic = pydantic_model_creator(City, name = "City")
CityIn_Pydantic = pydantic_model_creator(City, name="CityIn", exclude_readonly=True)

Country_Pydantic = pydantic_model_creator(Country, name = "Country")
CountryIn_Pydantic = pydantic_model_creator(Country, name = "PydanticIn", exclude_readonly=True)

Users_Pydantic = pydantic_model_creator(User, name = "Users")
UsersIn_Pydantic = pydantic_model_creator(User, name = "UsersIn", exclude_readonly=True)

