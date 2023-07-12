from sqlalchemy.orm import Session
from .core import BaseService
from ch04.persistence import UserRepository
from fastapi import Depends

from ch04.infrastructure.sqlite import get_session


class UserService(BaseService[UserRepository]):
    def __init__(
        self,
        repository: type[UserRepository] = UserRepository,
        session: Session = Depends(get_session),
    ) -> None:
        super().__init__(repository, session)

    def get_all(self):
        return self.repository.get_all()

    def get_by_id(self, id: int):
        return self.repository.get_by_id(id)
