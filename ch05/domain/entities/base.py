from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    all entitiy classes should inherits from this Base class
    >>> class Example(Base):
    ...     ...
    """
