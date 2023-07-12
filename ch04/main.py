from fastapi import FastAPI, Request, Depends
from .infrastructure.sqlite import engine
from .domain.entities import Base
from .presentation.v1 import v1_router

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


# used in oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# where other endpoints will token depends (oauth2_schema)
@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    print(form_data.username)
    try:
        user: user_model.User = user_db_services.get_user(
            session=session, email=payload.username
        )
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )

    is_validated: bool = user.validate_password(payload.password)
    if not is_validated:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid user credentials"
        )

    return user.generate_token()
    # self.grant_type = grant_type
    #     self.username = username
    #     self.password = password
    #     self.scopes = scope.split()
    #     self.client_id = client_id
    #     self.client_secret = client_secret
    ...
