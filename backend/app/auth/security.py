# JWT
from jose import jwt

# Password hashing
from passlib.context import CryptContext

from datetime import (
    datetime,
    timedelta
)


# Clé secrète JWT
SECRET_KEY = "SUPER_SECRET_HANTAV00_KEY"

# Algorithme JWT
ALGORITHM = "HS256"

# Expiration token
ACCESS_TOKEN_EXPIRE_MINUTES = 60


# Configuration bcrypt
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# Hasher mot de passe
def hash_password(password: str):

    return pwd_context.hash(password)


# Vérifier mot de passe
def verify_password(
    plain_password,
    hashed_password
):

    return pwd_context.verify(
        plain_password,
        hashed_password
    )


# Créer JWT token
def create_access_token(
    data: dict
):

    to_encode = data.copy()

    expire = (
        datetime.utcnow()
        + timedelta(
            minutes=ACCESS_TOKEN_EXPIRE_MINUTES
        )
    )

    to_encode.update({
        "exp": expire
    })

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt