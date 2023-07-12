from ch04.persistence.core import BaseRepository
from typing import TypeVar, Generic
from sqlalchemy.orm import Session
from fastapi import Depends
from ch04.infrastructure.sqlite import get_session

Repository = TypeVar("Repository", bound=BaseRepository)


class BaseService(Generic[Repository]):
    """
    >>> class ExampleService(BaseService[Repository]):
    ...     ...
    """

    def __init__(
        self,
        repository: type[Repository],
        session: Session,
    ) -> None:
        self.repository = repository(session)
