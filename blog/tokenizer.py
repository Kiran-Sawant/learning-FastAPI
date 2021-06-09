from typing import Optional
from datetime import (datetime, timedelta)

from jose import (jwt, JWTError)
from fastapi import Depends
from sqlalchemy.orm import Session

from .schemas import TokenData
from .db_models import User
from .db import get_session

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    # encoding the email
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str, credentials_exception, session:Session = Depends(get_session)):
    """Verifies a JWT by decoding the credential in it, queries the DB with that credential,
    returns the ORM model instance. raise ccredentials_exception if anything goes wrong."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWTError:
        raise credentials_exception
    
    user = session.query(User).filter(User.email == token_data.email).first()

    if user is None:
        raise credentials_exception
    return user
    