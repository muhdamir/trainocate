from ch04.domain.entities.users import Users
from .core import BaseRepositoryInterface
from ch04.domain.entities import Users


class UserRepositoryInterface(BaseRepositoryInterface[Users]):
    pass
