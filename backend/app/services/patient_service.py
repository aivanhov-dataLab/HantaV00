# Session SQLAlchemy
from sqlalchemy.orm import Session

# Modèle Patient
from app.models.patient import Patient

# Schémas Pydantic
from app.schemas.patient import (
    PatientCreate,
    PatientUpdate
)


# Création patient
def create_patient(
    db: Session,
    patient: PatientCreate
):

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


# Récupérer patient par ID
def get_patient_by_id(
    db: Session,
    patient_id: int
):

    return (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )


# Mise à jour patient
def update_patient(
    db: Session,
    patient_id: int,
    patient_data: PatientUpdate
):

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not patient:
        return None

    patient.status = patient_data.status
    patient.security_level = patient_data.security_level

    db.commit()

    db.refresh(patient)

    return patient


# Suppression patient
def delete_patient(
    db: Session,
    patient_id: int
):

    patient = (
        db.query(Patient)
        .filter(Patient.id == patient_id)
        .first()
    )

    if not patient:
        return False

    db.delete(patient)

    db.commit()

    return True