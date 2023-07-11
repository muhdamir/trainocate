from fastapi import FastAPI
from ch01.router import test_router
from ch03.main import ch03

app = FastAPI(
    title="TraiocatE API",
    summary="""
    This is the documentation for TrainocatE API.
    """,
    version="0.1.0",
)

app.include_router(router=test_router)
app.mount("/ch03", ch03)
