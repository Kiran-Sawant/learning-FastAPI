from datetime import timedelta

from fastapi import (APIRouter, Depends, HTTPException, status)
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from ..schemas import Login
from .. import db_models
from ..db import get_session
from ..hashing import verify
from ..tokenizer import (create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES)

router = APIRouter(
    tags=['Authentication']
)

@router.post("/login")
def login(request:OAuth2PasswordRequestForm = Depends(), session:Session = Depends(get_session)):

    user = session.query(db_models.User).filter(db_models.User.email == request.username).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with email {request.username} not found.")
    
    if not verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"Wrong password for {request.username}!")

    # if password correct, create a JWT token and send
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
  