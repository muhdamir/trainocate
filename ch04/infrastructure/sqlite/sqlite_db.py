from sqlalchemy import URL
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Engine, create_engine
from typing import Iterator

# connection_str = URL(
#     drivername="sqlite",
#     database="ch04.db",
#     host="/./ch04/infrastructure/sqlite",
#     username=None,
#     password=None,
#     port=None,
#     query=None,
# )

connection_str = "sqlite:///./ch04/infrastructure/sqlite/blog_app.db"

print(connection_str)
engine: Engine = create_engine(
    url=connection_str,
    echo=True,
    connect_args={"check_same_thread": False},
)

AppSession = sessionmaker(bind=engine)


def get_session() -> Iterator[Session]:
    session = AppSession()
    print("new session created")
    try:
        print("yielding a new session")
        yield session
    except Exception as e:
        print("error with session")
        session.rollback()
    finally:
        print("closing session")
        session.close()
        print("session closed")
