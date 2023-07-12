from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

engine = create_engine(
    "sqlite:///./ch03/infrastructure/sqlite/test.db",
    echo=True,
    connect_args={"check_same_thread": False},
)

AppSession = sessionmaker(bind=engine)


def get_session():
    """
    Get new session on each request
    """
    session: Session = AppSession()
    print("session started")
    try:
        yield session
    except:
        session.rollback()
    finally:
        print("session is closed")
        session.close()
