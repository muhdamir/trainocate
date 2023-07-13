from fastapi import APIRouter
from ch05.service.auth_service import AuthService
from ch05.service.blog_service import BlogService
from fastapi import Depends

blog_router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
)

from pydantic import BaseModel


class BlogData(BaseModel):
    blog_title: str
    # blog_author: int
    blog_image: str


@blog_router.get("/")
async def get_blog(
    blog_service: BlogService = Depends(),
    auth_token: dict = Depends(AuthService.token_checker),
):
    return blog_service.get_blog_by_user_id(auth_token)


@blog_router.post("/")
async def post_blog(
    blog_data: BlogData,
    blog_service: BlogService = Depends(),
    auth_token: dict = Depends(AuthService.token_checker),
):
    return blog_service.create(blog_data, auth_token)
