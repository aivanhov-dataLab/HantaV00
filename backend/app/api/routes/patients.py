# FastAPI router
from fastapi import (
    APIRouter,
    Depends,
    HTTPException
)

# SQLAlchemy session
from sqlalchemy.orm import Session

# DB dependency
from app.db.database import get_db

# Services
from app.services.patient_service import (
    create_patient,
    get_patients,
    get_patient_by_id,
    update_patient,
    delete_patient
)

# Schemas
from app.schemas.patient import (
    PatientCreate,
    PatientUpdate,
    PatientResponse
)


# Router patients
router = APIRouter(
    prefix="/patients",
    tags=["Patients"]
)


# CREATE patient
@router.post(
    "/",
    response_model=PatientResponse
)
def create_new_patient(
    patient: PatientCreate,
    db: Session = Depends(get_db)
):

    return create_patient(db, patient)


# READ all patients
@router.get(
    "/",
    response_model=list[PatientResponse]
)
def read_patients(
    db: Session = Depends(get_db)
):

    return get_patients(db)


# READ patient by ID
@router.get(
    "/{patient_id}",
    response_model=PatientResponse
)
def read_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    patient = get_patient_by_id(
        db,
        patient_id
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# UPDATE patient
@router.put(
    "/{patient_id}",
    response_model=PatientResponse
)
def update_existing_patient(
    patient_id: int,
    patient_data: PatientUpdate,
    db: Session = Depends(get_db)
):

    patient = update_patient(
        db,
        patient_id,
        patient_data
    )

    if not patient:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return patient


# DELETE patient
@router.delete("/{patient_id}")
def delete_existing_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):

    deleted = delete_patient(
        db,
        patient_id
    )

    if not deleted:

        raise HTTPException(
            status_code=404,
            detail="Patient not found"
        )

    return {
        "message": "Patient deleted successfully"
    }