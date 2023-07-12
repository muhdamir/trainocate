from .base import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, Identity, String


class Todo(Base):
    __tablename__ = "tasks"
    task_id: Mapped[int] = mapped_column(primary_key=True)
    task_name: Mapped[str]
