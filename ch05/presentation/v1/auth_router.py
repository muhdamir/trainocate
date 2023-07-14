from fastapi import APIRouter, Depends
from ch05.infrastructure.oauth import oauth2_scheme
from fastapi.security import OAuth2PasswordRequestForm
from ch05.service.auth_service import AuthService
from pydantic import BaseModel, EmailStr

auth_router = APIRouter(
    prefix="/auth",
    tags=["authorization"],
)


class User(BaseModel):
    email: EmailStr
    password: str


@auth_router.post("/login")
async def login(
    oauth_form: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(),
):
    """
    login will return token
    which means need to add logic for token creation
    My favorite search engine is [Duck Duck Go](#operations-authorization-signup_v1_auth_signup_post "The best search engine for privacy").
    """
    token = auth_service.login(oauth_form)
    return token
    """
    login will return token
    which means need to add logic for token creation
    My favorite search engine is [Duck Duck Go](https://duckduckgo.com "The best search engine for privacy").
    """


@auth_router.post("/signup")
async def signup(
    signup_data: User,
    auth_service: AuthService = Depends(),
):
    new_user = auth_service.signup(signup_data)
    return new_user


@auth_router.get("/profile")
async def test_authentication(
    auth_token: dict = Depends(AuthService.token_checker),
    auth_service: AuthService = Depends(),
):
    user = auth_service.get_user_by_id(auth_token.get("user_id"))

    return user
