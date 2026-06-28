from fastapi import APIRouter, Depends
from models import User, Users_Pydantic, UsersIn_Pydantic
import pass_hashing
import oauth2

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/")
async def create_user(user: UsersIn_Pydantic):
    # Hash password before saving
    user_data = user.dict()
    user_data["password"] = pass_hashing.Hash.bcrypt(user_data["password"])
    user_obj = await User.create(**user_data)
    return await Users_Pydantic.from_tortoise_orm(user_obj)

@router.get("/me")
async def get_me(current_user: str = Depends(oauth2.get_current_user)):
    user = await User.get(email=current_user)
    return await Users_Pydantic.from_tortoise_orm(user)



### Very Very Important Note:

# How to Protect Any Route

# Just add Depends(oauth2.get_current_user) to any route you want to protect
