from ch05.domain.entities.users import Users
from .core import BaseRepositoryInterface
from ch05.domain.entities import Users


class UserRepositoryInterface(BaseRepositoryInterface[Users]):
    pass
