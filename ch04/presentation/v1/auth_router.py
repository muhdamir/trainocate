from fastapi import APIRouter, Depends
from ch04.application.service import UserService
from ch04.presentation.dependency import user_service_caller
from ch04.infrastructure.oauth import oauth2_scheme

auth_router = APIRouter(
    prefix="/authorization",
    tags=["authorization"],
)


@auth_router.get("/ping")
async def ping(
    token: str = Depends(oauth2_scheme),
    service: UserService = Depends(),
):
    print(token)
    user = service.get_all()
    return user
