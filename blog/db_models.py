"""A module for defining SQLAlchemy ORM models"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, String, Integer, Float, ForeignKey)
from sqlalchemy.orm import relationship

Base = declarative_base()

class Blog(Base):
    __tablename__ = "blogs"

    id      = Column(Integer, primary_key=True, index=True)
    title   = Column(String)
    body    = Column(String)

    author_id   = Column(Integer, ForeignKey("users.id"))       # users is table name
    author      = relationship("User", back_populates='blogs')

class User(Base):
    __tablename__ = "users"

    id          = Column(Integer, primary_key=True, index=True)
    name        = Column(String)
    email       = Column(String)
    password    = Column(String)

    blogs       = relationship("Blog", back_populates='author')