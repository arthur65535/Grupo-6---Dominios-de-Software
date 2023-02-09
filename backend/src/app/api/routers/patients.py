from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.patient import Patient, PatientCreate, PatientRead
from app.models.transference_request import TransferenceRequest
from app.repository import patient_repository


Patient.update_forward_refs(
    TransferenceRequest=TransferenceRequest
)


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_patient(
    patient: PatientCreate,
    db: Session = Depends(get_session)
) -> PatientRead:

    return patient_repository.create_patient(
        patient=patient, db=db)


@router.get('/')
def get_all_patients(
        db: Session = Depends(get_session)
) -> list[PatientRead]:

    return patient_repository.get_all_patients(db=db)


@router.get('/{id}')
def get_patient_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> PatientRead:

    return patient_repository.get_patient_by_id(id=id, db=db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_by_id(id: int, db: Session = Depends(get_session)):
    patient_repository.delete_patient_by_id(id=id, db=db)
