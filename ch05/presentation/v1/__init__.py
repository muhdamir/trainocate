from fastapi import APIRouter
from .auth_router import auth_router
from .blog_router import blog_router

v1_router = APIRouter(prefix="/v1")
v1_router.include_router(auth_router)
v1_router.include_router(blog_router)
