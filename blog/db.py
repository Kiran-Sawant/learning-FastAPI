"""A module for configuring database through SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from . import db_models

# database connection string.
SQLALCHEMY_DB_URL = "sqlite:///.blog.db"

# creating engine ie. connecting with db engine.
engine = create_engine(SQLALCHEMY_DB_URL, connect_args={"check_same_thread": False})

# creating tables.
# db_models.Base.metadata.create_all(bind=engine)

# creating session factory binded to engine.
session_factory = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# session mannager function
def get_session():
    session = session_factory()
    try:
        yield session
    finally:
        session.close()