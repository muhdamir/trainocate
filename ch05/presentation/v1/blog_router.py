from fastapi import APIRouter
from ch05.service.auth_service import AuthService
from ch05.service.blog_service import BlogService
from fastapi import Depends

blog_router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
)


@blog_router.get("/")
async def get_blog(
    blog_service: BlogService = Depends(),
    auth_token: dict = Depends(AuthService.token_checker),
):
    return blog_service.get_blog_by_user_id(auth_token)
