# BaseModel Pydantic
from pydantic import BaseModel, Field


# Création patient
class PatientCreate(BaseModel):

    # Identifiant anonymisé
    anonymous_id: str

    # Statut médical
    status: str

    # Niveau sécurité :
    # 1 = surveillance
    # 2 = modéré
    # 3 = critique
    security_level: int = Field(
        ge=1,
        le=3
    )


# Mise à jour patient
class PatientUpdate(BaseModel):

    status: str

    security_level: int = Field(
        ge=1,
        le=3
    )


# Réponse API
class PatientResponse(BaseModel):

    id: int
    anonymous_id: str
    status: str
    security_level: int

    class Config:
        from_attributes = True