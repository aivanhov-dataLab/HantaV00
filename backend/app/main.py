# FastAPI principal
from fastapi import FastAPI

# Import du router patients
from app.api.routes.patients import router as patients_router

# Import de la base SQLAlchemy
from app.db.database import engine, Base

# Import du modèle Patient
# IMPORTANT :
# ce modèle doit être importé pour que SQLAlchemy
# détecte automatiquement la table patients
from app.models.patient import Patient

# Importer le user dans main.py
from app.models.user import User

# Add route auth to main.py
from app.api.routes import auth

# Création automatique des tables SQL
Base.metadata.create_all(bind=engine)


# Initialisation de l'application FastAPI
app = FastAPI(
    title="HantaV00 API",
    description="Epidemiological and hospital management system",
    version="1.0.0"
)


# Enregistrement des routes patients
app.include_router(patients_router)
# Inclureles route auth
app.include_router(auth.router)


# Route principale API
@app.get("/")
def root():
    return {
        "project": "HantaV00",
        "status": "running"
    }