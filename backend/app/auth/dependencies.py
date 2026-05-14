# JWT decoding
from jose import jwt, JWTError

# FastAPI
from fastapi import (
    Depends,
    HTTPException,
    status
)

# OAuth2
from fastapi.security import OAuth2PasswordBearer

# SQLAlchemy session
from sqlalchemy.orm import Session

# DB dependency
from app.db.database import get_db

# User model
from app.models.user import User

# JWT config
from app.auth.security import (
    SECRET_KEY,
    ALGORITHM
)


# OAuth2 bearer token
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)


# Utilisateur courant
def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    credentials_exception = HTTPException(

        status_code=status.HTTP_401_UNAUTHORIZED,

        detail="Could not validate credentials",

        headers={
            "WWW-Authenticate": "Bearer"
        }
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username: str = payload.get("sub")

        if username is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    user = (
        db.query(User)
        .filter(User.username == username)
        .first()
    )

    if user is None:
        raise credentials_exception

    return user