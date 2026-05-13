# APIRouter FastAPI
from fastapi import APIRouter, Depends

# Session SQLAlchemy
from sqlalchemy.orm import Session

# Dépendance DB
from app.db.database import get_db

# Services métier
from app.services.patient_service import (
    create_patient,
    get_patients
)

# Schémas Pydantic
from app.schemas.patient import (
    PatientCreate,
    PatientResponse
)


# Router patients
router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# Route création patient
@router.post("/", response_model=PatientResponse)
def create_new_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    return create_patient(db, patient)


# Route liste patients
@router.get("/", response_model=list[PatientResponse])
def read_patients(
    db: Session = Depends(get_db)
):

    return get_patients(db)