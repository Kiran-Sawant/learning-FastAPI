from passlib.context import CryptContext    # for hasshing password

# creating password hasher context
pwd_cxt = CryptContext(schemes=['bcrypt'], deprecated='auto')

def encrypt(password:str)->str:
    return pwd_cxt.hash(password)

def verify(hash_pwd:str, login_pwd:str)->bool:
    return pwd_cxt.verify(login_pwd, hash_pwd)