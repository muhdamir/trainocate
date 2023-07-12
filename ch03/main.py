from fastapi import FastAPI

from ch03.routers import template_router, todo_router


ch03 = FastAPI(
    title="TrainocatE CH03 FastAPI Endpoints",
)

# include router
ch03.include_router(todo_router)
ch03.include_router(template_router)
