from fastapi import FastAPI
from ch01.router import test_router
from ch03.main import ch03
from ch03.infrastructure.sqlite import engine
from ch03.schema import Base

# create FastAPI app
app = FastAPI(
    title="TraiocatE API",
    summary="""
    This is the documentation for TrainocatE API.
    """,
    version="0.1.0",
)


@app.on_event("startup")
def startup_task():
    # create all tables
    Base.metadata.create_all(bind=engine)


# mount sub application
app.mount("/ch03", ch03)

# include routers
app.include_router(router=test_router)
