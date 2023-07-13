from sqlalchemy.orm import Session
from fastapi import Depends
from ch04.infrastructure.sqlite import get_session


class BaseRepository:
    def __init__(
        self,
        session: Session = Depends(get_session),
    ) -> None:
        self.session = session
