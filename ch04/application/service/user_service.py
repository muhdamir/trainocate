from sqlalchemy.orm import Session
from .core import BaseService
from ch04.persistence import UserRepository
from fastapi import Depends

from ch04.infrastructure.sqlite import get_session


class UserService(BaseService[UserRepository]):
    def __init__(self, repository: UserRepository = Depends()) -> None:
        self.repository = repository

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)
