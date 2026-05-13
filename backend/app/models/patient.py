# Import des types SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import de la base SQLAlchemy
from app.db.database import Base


# Modèle Patient
# Représente la table patients dans PostgreSQL
class Patient(Base):

    # Nom réel de la table SQL
    __tablename__ = "patients"

    # Clé primaire
    id = Column(Integer, primary_key=True, index=True)

    # Identifiant anonymisé patient
    anonymous_id = Column(String, unique=True, index=True)

    # Statut médical du patient
    status = Column(String)

    # Niveau de sécurité :
    # 1 = surveillance
    # 2 = risque modéré
    # 3 = critique
    security_level = Column(Integer)