from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schemas
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

# SECRET KEY
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# Algorithm
ALGORITHM = "HS256"
# Expiration Time
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    # In order to create the encoded jwt, we first make a copy of the inputted dictionary object (data)
    to_encode = data.copy()
    # then we use the imported datetime module to: create an expire time by taking this moment + 30min
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    # then we add the expire time to the dict using update
    # remember that in order to update with the new object inside the dict, we need to do it with {"expire": expire}
    to_encode.update({"exp": expire})
    # then we encode it
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:

        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except JWTError:
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail=f"Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})
    return verify_access_token(token, credentials_exception)
