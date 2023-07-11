from pydantic import BaseModel


class TestDataResponseModel(BaseModel):
    task_id: int
    task_name: str


class TestDataPostModel(BaseModel):
    task_name: str


class TestDataPatchModel(TestDataPostModel):
    pass
