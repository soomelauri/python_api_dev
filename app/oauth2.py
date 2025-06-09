from jose import jwt, JWTError
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timezone
from sqlalchemy.orm import Session
from .config import settings


oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

def create_access_token(data: dict):
    # In order to create the encoded jwt, we first make a copy of the inputted dictionary object (data)
    to_encode = data.copy()
    # then we use the imported datetime module to: create an expire time by taking this moment + 30min
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_expire_minutes)
    # then we add the expire time to the dict using update
    # remember that in order to update with the new object inside the dict, we need to do it with {"expire": expire}
    to_encode.update({"exp": expire})
    # then we encode it
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.algorithm])
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception
        token_data = schemas.TokenData(id=id)

    except JWTError as e:
        print(f"JWTError occurred: {e}")
        raise credentials_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                                          detail=f"Could not validate credentials", 
                                          headers={"WWW-Authenticate": "Bearer"})
    
    token = verify_access_token(token, credentials_exception)

    user = db.query(models.User).filter(models.User.id == token.id).first()
    print(user)

    return user
