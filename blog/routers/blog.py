from typing import List

from fastapi import (APIRouter, Depends, status, HTTPException)
from sqlalchemy.orm import Session

from .. import db_models
from ..db import get_session
from ..schemas import (Blog_Detail, Blog, User)
from ..crud import bCrud
from ..oauth2 import get_current_user

router = APIRouter(
    prefix= "/blog",
    tags=["blogs"]
)

#_________________________Blog API routers________________________#
"""In the router given below, Depends is a dependency injector.
A dependency injector executes the passed function inline, and
stores the return value of the function in the variable(session).
create_blog() requires a SQA session to interact with the database.
However, creating and yielding a session is managed by the get_session
function in db module, therefore it is a dependency for create_blog().
Depends() executes that function and passes the session to session variable,
and typehinting helps with intelliscence. make sure that function returns datatype
as mentioned in the type hint. this process is called dependency injection."""

@router.post("/create", status_code=status.HTTP_201_CREATED, response_model=Blog_Detail)
def create_blog(request:Blog, session:Session = Depends(get_session), current_user:User = Depends(get_current_user)):

    # new_blog = db_models.Blog(title=request.title, body=request.body, author_id=request.author_id)
    # session.add(new_blog)
    # session.commit()
    # session.refresh(new_blog)

    return bCrud.create(request, session)

@router.get("/", response_model=List[Blog_Detail])
def get_all_blogs(session:Session = Depends(get_session), current_user:User = Depends(get_current_user)):

    # blogs = session.query(db_models.Blog).all()

    return bCrud.get_all(session)

@router.get("/get/{id}", status_code=200, response_model=Blog_Detail)
def get_blog(id:int, session:Session = Depends(get_session), current_user:User = Depends(get_current_user)):

    # blog = session.query(db_models.Blog).filter(db_models.Blog.id == id).first()

    # if not blog:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
    #                         detail=f"Blog with {id} is not available")

    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {"detail": f"Blog with {id} is not available"}
    # else:
    #     return blog

    return bCrud.get(id, session)

@router.put("/update/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id:int, request:Blog, session:Session = Depends(get_session), current_user:User = Depends(get_current_user)):

    # blog = session.query(db_models.Blog).filter(db_models.Blog.id == id)
    # if not blog.first():
    #     raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
    # else:
    #     blog.update(request)
    #     session.commit()
    
    return bCrud.update(id, request, session)

@router.delete("/delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, session:Session = Depends(get_session), current_user:User = Depends(get_current_user)):
    
    # blog = session.query(db_models.Blog).filter(db_models.Blog.id == id)

    # if not blog.first():
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} does not exist.")
    # else:
    #     blog.delete(synchronize_session=False)
    #     session.commit()
    
    # return f'Blog {id} deleted'

    return bCrud.delete(id, session)