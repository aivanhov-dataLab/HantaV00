# SQLAlchemy columns
from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean
)

# Base SQLAlchemy
from app.db.database import Base


# Modèle utilisateur
class User(Base):

    __tablename__ = "users"

    # ID utilisateur
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Nom utilisateur unique
    username = Column(
        String,
        unique=True,
        index=True
    )

    # Email utilisateur
    email = Column(
        String,
        unique=True,
        index=True
    )

    # Mot de passe hashé
    hashed_password = Column(String)

    # Rôle utilisateur
    # admin / hospital / analyst
    role = Column(String)

    # Compte actif
    is_active = Column(
        Boolean,
        default=True
    )