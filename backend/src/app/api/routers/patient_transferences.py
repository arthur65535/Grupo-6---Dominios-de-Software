from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.repository import patient_transference_repository
from app.db.database import get_session
from app.models.patient_transference import (
    PatientTransferenceReadDenormalized
)


router = APIRouter()


@router.get('/{id}')
def get_patient_transference_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> PatientTransferenceReadDenormalized:

    return patient_transference_repository.get_patient_transference_by_id(
        id=id, db=db)


@router.get('/')
def get_all_patient_transferences(
    db: Session = Depends(get_session)
) -> list[PatientTransferenceReadDenormalized]:

    return patient_transference_repository.get_all_patient_transferences(db=db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_patient_transference_by_id(
    id: int,
    db: Session = Depends(get_session),
):

    patient_transference_repository.delete_patient_transference_by_id(
        id=id, db=db)
