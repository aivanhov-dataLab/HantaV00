# Session SQLAlchemy
from sqlalchemy.orm import Session

# Modèle Patient
from app.models.patient import Patient

# Schéma Pydantic
from app.schemas.patient import PatientCreate


# Création patient
def create_patient(db: Session, patient: PatientCreate):

    db_patient = Patient(

        anonymous_id=patient.anonymous_id,
        status=patient.status,
        security_level=patient.security_level
    )

    db.add(db_patient)

    db.commit()

    db.refresh(db_patient)

    return db_patient


# Récupérer tous les patients
def get_patients(db: Session):

    return db.query(Patient).all()