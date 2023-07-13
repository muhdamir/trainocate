from fastapi import FastAPI
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


app.include_router(v1_router)
