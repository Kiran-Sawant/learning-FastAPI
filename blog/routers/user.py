from fastapi import (APIRouter, Depends, Response, status, HTTPException)
from sqlalchemy.orm import Session

from ..schemas import (User_detail, User)
from ..db import get_session
from .. import db_models
from ..hashing import encrypt
from ..crud import uCrud


router = APIRouter(
    prefix="/user",
    tags=['user']
)

@router.post("/create", response_model=User_detail)
def create_user(request:User, session:Session = Depends(get_session)):

    # new_user = db_models.User(name=request.name, email=request.email, password=encrypt(request.password))
    # session.add(new_user)
    # session.commit()
    # session.refresh(new_user)
    # return new_user

    return uCrud.create(request, session)

@router.get("/get/{id}", status_code=status.HTTP_200_OK, response_model=User_detail)
def get_user(id:int, response: Response, session:Session = Depends(get_session)):

    # user = session.query(db_models.User).filter(db_models.User.id == id).first()
    # if not user:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with ID {id} not found")
    # else:
    #     return user

    return uCrud.get_user(id, session)