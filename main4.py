# request body, POST methods

from fastapi import FastAPI
from typing import (Tuple, List, Callable, Awaitable, Generator, Optional)
from pydantic import BaseModel
import uvicorn

# creating FastApi instance.
app = FastAPI()

@app.get("/")
def home():
    return {"home": "welcome to home page"}

# passing URL query parameters as function argument.
# URL will be like domain/blog?limit=5&published=true&sort=str
@app.get('/blog')
def index(limit:int = 10, published:bool = True, sort:Optional[str] = None):
    # only get 10 published blogs
    if published:
        return {"data": f"{limit} published blogs from the db"}
    else:
        return {"data": f"{limit} blogs from the db"}

@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'all unpublished blogs'}

# dynamic routing
@app.get('/blog/{id}')
def show_blog(id:int):
    # fetch blog with id == id
    return {"data": id}

#---move static routes above dynamic routes.
# @app.get("/blog/unpublished")
# def unpublished():
#     return {'data': 'all unpublished blogs'}

# path parameters must be in the .get()
# query parmeters must be inside the function arguments.
@app.get('/blog/{id}/comments')
def comments(id:int, limit:int= 10):
    # fetch comments with id == id
    return {"data": {'comments': [{'user1': 'comment'}, {'user2': 'comment'}]}}

# blog model, request body
class Blog(BaseModel):
    title:str
    body:str
    published:Optional[bool] 

# POST method API view
@app.post("/blog")
def create_blog(request:Blog):  # request schema will be of Blog type.
    # return request
    return {'data': f'blog created with title {request.title}'}

# For debugging
# if __name__ == "__main__":
    # uvicorn.run(app, host="127.0.0.1", port=9000)