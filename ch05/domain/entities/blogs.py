from .base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, func
from datetime import datetime
from .users import Users


class Blogs(Base):
    __tablename__ = "blogs"
    blog_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    blog_title: Mapped[str]
    blog_author: Mapped[int] = mapped_column(
        ForeignKey("users.user_id"),
    )
    blog_image: Mapped[str]
    blog_date_created: Mapped[datetime] = mapped_column(
        server_default=func.now(),
    )
    blog_date_updated: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    # relationship
    user: Mapped[Users] = relationship("Users", back_populates="blogs")
