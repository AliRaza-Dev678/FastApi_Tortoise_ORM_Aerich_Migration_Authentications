from fastapi import APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends
from models import User
import pass_hashing
import jwt_token

router = APIRouter(tags=["Authentication"])

@router.post("/login")
async def login(request: OAuth2PasswordRequestForm = Depends()):
    # Find user by email
    user = await User.get_or_none(email=request.username)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Invalid credentials"
        )
    # Verify password
    if not pass_hashing.Hash.verify(user.password, request.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid password"
        )
    # Create token
    token = jwt_token.create_access_token(data={"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}