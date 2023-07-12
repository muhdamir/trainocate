from pydantic import BaseModel
from typing import Optional


class TodoResponseModel(BaseModel):
    task_id: int
    task_name: str

    class Config:
        from_attributes = True


class TodoPostModel(BaseModel):
    task_name: str


class TodoPatchModel(BaseModel):
    task_name: Optional[str]
