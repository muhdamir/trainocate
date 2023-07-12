from fastapi import APIRouter, Depends, Request, Form
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ch03.schema import Todo
from ch03.models import TodoResponseModel

from ch03.infrastructure.sqlite import get_session

template_router = APIRouter(
    prefix="/templates",
    tags=["Templates"],
)

templates = Jinja2Templates("./ch03/templates")


@template_router.get("/")
async def get_template(
    request: Request,
    session: Session = Depends(get_session),
):
    data = session.query(Todo).all()
    data = [TodoResponseModel.model_validate(dat).model_dump() for dat in data]
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "data": data,
        },
    )


@template_router.post("/")
async def post_task(
    requests: Request,
    session: Session = Depends(get_session),
    task_name: str = Form(...),
):
    new_data = Todo(task_name=task_name)
    session.add(new_data)
    session.commit()
    data = session.query(Todo).all()
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": requests,
            "data": data,
        },
    )


@template_router.delete("/{task_id}")
async def delete_task(
    task_id: int,
    session: Session = Depends(get_session),
):
    target_data = session.query(Todo).get(task_id)
    session.delete(target_data)
    session.commit()
    return {"message": "Successful"}
