from fastapi import (HTTPException, status)
from sqlalchemy.orm import Session

from .. import db_models
from ..schemas import Blog

def get_all(session:Session)->list:

    blogs = session.query(db_models.Blog).all()

    return blogs

def create(request:Blog, session:Session):

    new_blog = db_models.Blog(title=request.title, body=request.body, author_id=request.author_id)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)

    return new_blog

def get(id:int, session:Session):

    blog = session.query(db_models.Blog).filter(db_models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID {id} not found.")
    else:
        return blog

def update(id:int, request:Blog, session:Session):

    blog = session.query(db_models.Blog).filter(db_models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Blog with ID {id} not found")
    else:
        blog.update(request)
        session.commit()

    return {"detail": "succexx"}

def delete(id:int, session:Session):

    blog = session.query(db_models.Blog).filter(db_models.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with ID:{id}, not found.")
    else:
        blog.delete(synchronize_session=False)
        session.commit()
    
    return {"details": "Blog {id} deleted!"}

