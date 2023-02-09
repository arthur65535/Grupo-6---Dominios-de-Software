from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.patient_transference import PatientTransference
from app.models.transference_request import (
    TransferenceRequest,
    TransferenceRequestCreate,
    TransferenceRequestRead,
    TransferenceRequestReadDenormalized
)
from app.models.patient_transference import (
    PatientTransference,
    PatientTransferenceCreate,
    PatientTransferenceRead,
    PatientTransferenceReadDenormalized
)
from app.repository import patient_transference_repository
from app.repository import transference_request_repository


TransferenceRequest.update_forward_refs(
    PatientTransference=PatientTransference
)

TransferenceRequestReadDenormalized.update_forward_refs(
    PatientTransference=PatientTransference
)


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_transference_request(
    transference_request: TransferenceRequestCreate,
    db: Session = Depends(get_session)
) -> TransferenceRequestRead:

    return transference_request_repository.create_transference_request(
        transference_request=transference_request, db=db)


@router.get('/')
def get_all_transference_requests(
        db: Session = Depends(get_session)
) -> list[TransferenceRequestReadDenormalized]:

    return transference_request_repository.get_all_transference_requests(db=db)


@router.get('/{id}')
def get_transference_request_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> TransferenceRequestReadDenormalized:

    return transference_request_repository.get_transference_request_by_id(
        id=id, db=db)


@router.post('/{transference_request_id}/patient-transferences/')
def create_patient_transference_for_transference_request(
    transference_request_id: int,
    patient_transference: PatientTransferenceCreate,
    db: Session = Depends(get_session)
) -> PatientTransferenceRead:

    return patient_transference_repository.create_patient_transference(
        transference_request_id=transference_request_id,
        patient_transference=patient_transference,
        db=db
    )


@router.get('/{transference_request_id}/patient-transferences/')
def get_patient_transference_of_transference_request(
    transference_request_id: int,
    db: Session = Depends(get_session)
) -> PatientTransferenceReadDenormalized:

    return patient_transference_repository \
        .get_patient_transference_of_transference_request(
            transference_request_id=transference_request_id,
            db=db
        )


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_transference_request_by_id(
    id: int,
    db: Session = Depends(get_session)
):
    transference_request_repository.delete_transference_request_by_id(
        id=id, db=db)
