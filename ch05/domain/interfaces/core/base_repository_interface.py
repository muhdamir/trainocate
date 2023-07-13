from typing import Generic, TypeVar
from ch05.domain.entities import Base
from abc import ABC, abstractmethod

Entity = TypeVar("Entity", bound=Base)


class BaseRepositoryInterface(Generic[Entity], ABC):
    """
    All repository interface should inherit from this class
    >>> class Example(BaseRepositoryInterface[Entity]):
    ...     ...
    """

    @abstractmethod
    def get_all(
        self,
    ) -> list[Entity]:
        ...

    @abstractmethod
    def get_by_id(
        self,
        id: int,
    ) -> Entity:
        ...
