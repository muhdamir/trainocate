from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, func
from .base import Base
from datetime import datetime


class Users(Base):
    __tablename__ = "users"
    user_id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str]
    password: Mapped[str]
    user_date_created: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        default=func.now(),
    )
    user_date_updated: Mapped[datetime] = mapped_column(
        server_default=func.now(),
        server_onupdate=func.now(),
    )

    # relationship
    blogs = relationship("Blogs", back_populates="user")
