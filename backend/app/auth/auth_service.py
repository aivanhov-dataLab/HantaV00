# SQLAlchemy session
from sqlalchemy.orm import Session

# Modèle User
from app.models.user import User

# Schéma User
from app.schemas.user import UserCreate

# Sécurité JWT
from app.auth.security import (
    hash_password,
    verify_password
)


# Créer utilisateur
def create_user(
    db: Session,
    user: UserCreate
):

    db_user = User(

        username=user.username,
        email=user.email,

        # Password hashé
        hashed_password=hash_password(
            user.password
        ),

        role=user.role
    )

    db.add(db_user)

    db.commit()

    db.refresh(db_user)

    return db_user


# Trouver utilisateur par username
def get_user_by_username(
    db: Session,
    username: str
):

    return (
        db.query(User)
        .filter(User.username == username)
        .first()
    )


# Authentifier utilisateur
def authenticate_user(
    db: Session,
    username: str,
    password: str
):

    user = get_user_by_username(
        db,
        username
    )

    if not user:
        return None

    # Vérification password
    if not verify_password(
        password,
        user.hashed_password
    ):
        return None

    return user