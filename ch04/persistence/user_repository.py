from ch04.domain.entities.users import Users
from ch04.domain.interfaces import UserRepositoryInterface
from .core import BaseRepository


class UserRepository(
    BaseRepository,
    UserRepositoryInterface,
):
    def get_all(self) -> list[Users]:
        return self.session.query(Users).all()

    def get_by_id(self, id: int) -> Users:
        return self.session.query(Users).get(id)
