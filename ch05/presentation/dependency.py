from ch04.application.service import UserService
from ch04.infrastructure.sqlite import get_session
from fastapi import Depends
from sqlalchemy.orm import Session
from typing import TypeVar
from ch04.persistence import UserRepository
from ch04.persistence.core import BaseRepository
from ch04.application.service.core import BaseService

Repository = TypeVar("Repository", bound=BaseRepository)
Service = TypeVar("Service", bound=BaseService)


class ServiceCaller:
    def __init__(
        self,
        repository: type[Repository],
        service: type[Service],
    ) -> None:
        self.repository = repository
        self.service = service

    def __call__(
        self,
        session: Session = Depends(get_session),
    ) -> Service:
        instantiated_repo = self.repository(session)
        instantiated_service = self.service(instantiated_repo)
        return instantiated_service


user_service_caller = ServiceCaller(UserRepository, UserService)
