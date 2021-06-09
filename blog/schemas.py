from typing import List, Optional

from pydantic import BaseModel

# pydantic model
class User(BaseModel):
    name:str
    email:str
    password:str

    class Config():
        orm_mode = True


class Blog(BaseModel):
    title:str
    body: str
    author_id: int

    class Config():
        orm_mode = True


class User_detail(BaseModel):
    """response schema for user detail."""
    name:str
    email:str
    blogs:List[Blog] = []

    class Config():
        orm_mode = True
    

class Blog_Detail(BaseModel):
    title:str
    body:str
    author:User_detail

    class Config():
        orm_mode = True

class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None
