from sqlalchemy.orm import Session
from ch05.domain.entities import Users
from time import time
import jwt
from fastapi import Depends
from ch05.infrastructure.sqlite import get_session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import HTTPException
from fastapi import status
from ch05.infrastructure.oauth import oauth2_scheme
from jwt.exceptions import PyJWTError
from datetime import datetime
from pydantic import BaseModel, EmailStr


# from ch05.presentation.v1.auth_router import User
class User(BaseModel):
    email: EmailStr
    password: str


class AuthService:
    SECRET = "my_sercret"

    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session

    def get_user_by_id(
        self,
        user_id: int,
    ):
        user = self.session.query(Users).get(user_id)
        return user

    def get_user(
        self,
        username: str,
    ):
        user = self.session.query(Users).filter(Users.username == username).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return user

    def signup(
        self,
        signup_data: User,
    ):
        user = (
            self.session.query(Users)
            .filter(Users.username == signup_data.email)
            .first()
        )
        if user:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        user = Users(username=signup_data.email, password=signup_data.password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def login(
        self,
        form_data: OAuth2PasswordRequestForm,
    ):
        username = form_data.username
        password = form_data.password
        user = self.get_user(username)
        hashed_password = user.password
        # need to add hashing
        if hashed_password != password:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)
        token = self.create_access_token(user=user.username, user_id=user.user_id)
        return {"access_token": token, "token_type": "Bearer"}

    def create_access_token(
        self,
        user: str,
        user_id: int,
    ) -> str:
        payload = {
            "user": user,
            "user_id": user_id,
            "expires": time() + 36,
        }
        token = jwt.encode(payload, self.SECRET, algorithm="HS256")
        return token

    @classmethod
    def token_checker(
        cls,
        token: str = Depends(oauth2_scheme),
    ):
        try:
            decoded_data: dict = jwt.decode(token, cls.SECRET, algorithms=["HS256"])
            expire = decoded_data.get("expires")
            if not expire:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="No access token supplied",
                )
            if datetime.utcnow() > datetime.utcfromtimestamp(expire):
                raise HTTPException(
                    status_code=status.HTTP_403_FORBIDDEN, detail="Token expired!"
                )
            return decoded_data

        except PyJWTError:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid token"
            )
