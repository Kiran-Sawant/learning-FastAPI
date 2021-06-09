from fastapi import (HTTPException, status)
from sqlalchemy.orm import Session

from .. import db_models
from ..schemas import (User_detail, User)
from ..hashing import encrypt

def create(request:User, session:Session):

    new_user = db_models.User(name=request.name, email=request.email, password=encrypt(request.password))

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user

def get_user(id:int, session:Session):

    user = session.query(db_models.User).filter(db_models.User.id == id).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"No user with ID:{id}.")
    else:
        return user