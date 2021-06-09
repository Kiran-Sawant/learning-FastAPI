from fastapi import (FastAPI, Depends, status, Response, HTTPException)
from sqlalchemy.orm import Session

from .schemas import (Blog, Blog_Detail, User, User_detail)     # pydantic schemas
from . import db_models
from .hashing import encrypt
from .db import engine, get_session
from .routers import (blog, user, authentication)       # router modules

# initializing ASGI app
app = FastAPI()

# Update/Create tables based on ORM models
db_models.Base.metadata.create_all(bind=engine)

#_______adding routers to main_________#
"""One can separate API views into different modules in a routers
package and create router instances by decorating those views with
a router instance rather than a FastAPI() instance like here.
Then register those router instances with the FastAPI() instance in
main module."""
app.include_router(authentication.router)
app.include_router(blog.router)
app.include_router(user.router)


#___________________Blog API views______________________#

# @app.post("/blog/create", status_code=status.HTTP_201_CREATED, response_model=Blog_Detail, tags=['blogs'])
# def create_blog(request:Blog, session:Session = Depends(get_session)):

#     new_blog = db_models.Blog(title=request.title, body=request.body, author_id=request.author_id)
#     session.add(new_blog)
#     session.commit()
#     session.refresh(new_blog)

#     return new_blog

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, tags=['blogs'])
# def update_blog(id:int, request:Blog, session:Session = Depends(get_session)):

#     blog = session.query(db_models.Blog).filter(db_models.Blog.id == id)
#     if not blog.first():
#         raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found.")
#     else:
#         blog.update(request)
#         session.commit()
    
#     return "succsexx!"

# @app.delete("/blog/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=['blogs'])
# def delete_blog(id:int, session:Session = Depends(get_session)):
    
#     blog = session.query(db_models.Blog).filter(db_models.Blog.id == id)

#     if not blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog {id} does not exist.")
#     else:
#         blog.delete(synchronize_session=False)
#         session.commit()
    
#     return f'Blog {id} deleted'


# @app.get("/blog/{id}", status_code=200, response_model=Blog_Detail, tags=['blogs'])
# def get_blog(id:int, response: Response, session:Session = Depends(get_session)):

#     blog = session.query(db_models.Blog).filter(db_models.Blog.id == id).first()

#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#                             detail=f"Blog with {id} is not available")

#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {"detail": f"Blog with {id} is not available"}
#     else:
#         return blog

#___________________User API views______________________#

# @app.post("/user/create", response_model=User_detail, tags=['users'])
# def create_user(request:User, session:Session = Depends(get_session)):

    
#     new_user = db_models.User(name=request.name, email=request.email, password=encrypt(request.password))

#     session.add(new_user)
#     session.commit()
#     session.refresh(new_user)

#     return new_user

# @app.get("/user/{id}", status_code=status.HTTP_200_OK, response_model=User_detail, tags=['users'])
# def get_user(id:int, response: Response, session:Session = Depends(get_session)):

#     user = session.query(db_models.User).filter(db_models.User.id == id).first()
    
#     if not user:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
#     else:
#         return user
