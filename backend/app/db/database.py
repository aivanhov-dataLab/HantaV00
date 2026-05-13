# SQLAlchemy engine
from sqlalchemy import create_engine

# SQLAlchemy session
from sqlalchemy.orm import sessionmaker, declarative_base

# Chargement variables environnement
from dotenv import load_dotenv

import os


# Charger le fichier .env
load_dotenv()


# URL PostgreSQL
DATABASE_URL = os.getenv("DATABASE_URL")


# Création moteur SQLAlchemy
engine = create_engine(DATABASE_URL)


# Création session DB
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base des modèles SQLAlchemy
Base = declarative_base()


# Dépendance FastAPI
# Fournit une session DB à chaque requête API
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()