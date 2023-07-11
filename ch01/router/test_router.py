from fastapi import APIRouter, HTTPException, Depends
from ch01.models import TestDataResponseModel, TestDataPatchModel, TestDataPostModel
from typing import Optional
from ch01.infrastructure.sqlite import get_db
from sqlite3 import Cursor

test_router = APIRouter(
    prefix="/api/test_router",
    tags=["Test Endpoints"],
)


@test_router.get("/")
async def get_all_task(
    cursor: Cursor = Depends(get_db),
):
    query = cursor.execute("SELECT * FROM todo")
    return query.fetchall()


@test_router.get("/{task_id}")
async def get_by_task_id(
    task_id: int,
    cursor: Cursor = Depends(get_db),
):
    query = cursor.execute(f"SELECT * FROM todo WHERE task_id = {task_id}")
    return query.fetchone()


@test_router.post(
    "/",
    response_model=bool,
)
async def create_new_task(
    task_data: TestDataPostModel,
    cursor: Cursor = Depends(get_db),
):
    params = tuple(task_data.model_dump().values())
    query = cursor.execute(
        "INSERT INTO todo(task_name) VALUES (?)",
        params,
    )
    cursor.connection.commit()
    return True


@test_router.delete(
    "/{task_id}",
    response_model=bool,
)
async def delete_task(
    task_id: int,
    cursor: Cursor = Depends(get_db),
):
    query = cursor.execute(f"DELETE FROM todo WHERE task_id = {task_id}")
    cursor.connection.commit()
    return True
