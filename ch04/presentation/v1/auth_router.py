from fastapi import APIRouter, Depends
from ch04.application.service import UserService
from ch04.presentation.dependency import user_service_caller
from ch04.infrastructure.oauth import oauth2_scheme

auth_router = APIRouter(
    prefix="/authorization",
    tags=["authorization"],
)

import jwt
from jwt.exceptions import PyJWTError
from fastapi.exceptions import HTTPException
from fastapi import status
from datetime import datetime


def verify_access_token(token: str) -> dict:
    try:
        data: dict = jwt.decode(token, "aaaaaaaaaaa", algorithms=["HS256"])
        expire = data.get("expires")
        if expire is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No access token supplied",
            )
        if datetime.utcnow() > datetime.utcfromtimestamp(expire):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN, detail="Token expired!"
            )
        return data
    # other jwt error
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
        )


@auth_router.get("/ping")
async def ping(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(),
):
    print("woahhhhh")
    print(token)
    user = service.get_all()
    return user
