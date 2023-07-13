from fastapi import FastAPI, Request, Depends
from .infrastructure.sqlite import engine
from .domain.entities import Base
from .presentation.v1 import v1_router
from sqlalchemy.orm import Session
from .infrastructure.sqlite import get_session
from ch04.domain.entities import Users
from fastapi.exceptions import HTTPException
from fastapi import status
from fastapi.security import OAuth2AuthorizationCodeBearer

from ch04.infrastructure.oauth import oauth2_scheme

app = FastAPI(
    title="Event App's Endpoints",
    summary="This is the official documentation for TrainocatE's Event App's endpoints",
)


@app.on_event("startup")
async def startup_task():
    # create all table
    print("creating database, and tables")
    Base.metadata.create_all(bind=engine)
    print("database/tables created successfully")


# v1 api
app.include_router(v1_router)


from fastapi.security import OAuth2PasswordRequestForm

from time import time
import jwt


def create_access_token(user: str) -> str:
    # payload = {"user": user, "expires": time() + 3600}
    payload = {"user": user, "expires": time() + 36}
    token = jwt.encode(payload, "aaaaaaaaaaa", algorithm="HS256")
    return token


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


# used in oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# where other endpoints will token depends (oauth2_schema) with additional function
# create endpoint login using OAuth2PasswordRequestForm
@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    user = session.query(Users).filter(Users.username == form_data.username).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials",
        )
        # if error is raised it doesn even go to the next code
    print(user.password)
    print(form_data.password)
    password = user.password == form_data.password
    if not password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid user credentials",
        )

    created_access_token = create_access_token(user.username)
    print(created_access_token)
    if password:
        return {"access_token": created_access_token, "token_type": "Bearer"}


@app.get("/")
async def testing_auth(token: str = Depends(oauth2_scheme)):
    return verify_access_token(token)

    # try:
    #     user: user_model.User = user_db_services.get_user(
    #         session=session, email=payload.username
    #     )
    # except:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
    #     )

    # is_validated: bool = user.validate_password(payload.password)
    # if not is_validated:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
    #     )

    # return user.generate_token()
    # self.grant_type = grant_type
    #     self.username = username
    #     self.password = password
    #     self.scopes = scope.split()
    #     self.client_id = client_id
    #     self.client_secret = client_secret
    ...
