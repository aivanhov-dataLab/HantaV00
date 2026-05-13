# Import BaseModel Pydantic
from pydantic import BaseModel


# Schéma utilisé pour créer un patient
class PatientCreate(BaseModel):

    # Identifiant anonymisé
    anonymous_id: str

    # Statut médical
    status: str

    # Niveau de sécurité
    security_level: int


# Schéma utilisé pour retourner un patient
class PatientResponse(BaseModel):

    id: int
    anonymous_id: str
    status: str
    security_level: int

    # Compatibilité SQLAlchemy
    class Config:
        from_attributes = True