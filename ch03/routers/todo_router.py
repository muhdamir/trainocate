from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ch03.infrastructure.sqlite import get_session
from ch03.schema import Todo
from ch03.models import TodoResponseModel, TodoPostModel, TodoPatchModel


todo_router = APIRouter(prefix="/todo", tags=["To-do"])


@todo_router.get("/ping")
async def test_connection():
    return "pong"


@todo_router.get("/")
async def get_all_todos(
    session: Session = Depends(get_session),
):
    data = session.query(Todo).all()
    return data


@todo_router.get("/{task_id}")
async def get_by_id(
    task_id: int,
    session: Session = Depends(get_session),
):
    data = session.query(Todo).get(task_id)
    return data


@todo_router.post("/")
async def created_todos(
    todo_data: TodoPostModel,
    session: Session = Depends(get_session),
):
    new_data = Todo(**todo_data.model_dump())
    session.add(new_data)
    session.commit()
    session.refresh(new_data)
    return new_data


@todo_router.patch("/{task_id}")
async def update_todos(
    task_id: int,
    todo_data: TodoPatchModel,
    session: Session = Depends(get_session),
):
    target_data = session.query(Todo).get(task_id)
    target_attrs = todo_data.model_dump(exclude_unset=True)
    for k, v in target_attrs.items():
        setattr(target_data, k, v)
    session.commit()
    session.refresh(target_data)
    return target_data


@todo_router.delete("/{task_id}")
async def delete_todos(
    task_id: int,
    session: Session = Depends(get_session),
):
    target_data = session.query(Todo).get(task_id)
    session.delete(target_data)
    session.commit()
    return "Successful"
