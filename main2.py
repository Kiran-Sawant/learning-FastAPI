from fastapi import FastAPI
from typing import (Tuple, List, Callable, Awaitable, Generator, Optional)

# creating FastApi instance.
app = FastAPI()

# @api_instance.http_method("URL path")
@app.get('/')
def home():
    return {"data": "blog list"}


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

@app.get('/blog/{id}/coments')
def comments(id:int):
    # fetch comments with id == id
    return {"data": {'comments': [{'user1': 'comment'}, {'user2': 'comment'}]}}

@app.post("/blog")
def create_blog(name:str):
    return {"data": f"Blog {name} is created"}