from ch05.domain.entities import Blogs
from ch05.infrastructure.sqlite import get_session
from fastapi import Depends
from sqlalchemy.orm import Session


class BlogService:
    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session

    def get_blog_by_user_id(self, data: dict):
        user_id = data.get("user_id")
        blogs = self.session.query(Blogs).filter(Blogs.blog_author == user_id).all()
        return blogs
