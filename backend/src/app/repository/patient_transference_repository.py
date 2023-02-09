from fastapi import HTTPException, status
from sqlmodel import col, select, Session, and_

from app.models.patient_transference import (
    PatientTransference,
    PatientTransferenceCreate,
    PatientTransferenceRead,
    PatientTransferenceReadDenormalized,
    PatientTransferenceStatus
)
from app.repository import transference_request_repository


def create_patient_transference(
    transference_request_id: int,
    patient_transference: PatientTransferenceCreate,
    db: Session
) -> PatientTransferenceRead:

    transference_request = transference_request_repository \
        .get_transference_request_by_id(id=transference_request_id, db=db)

    if not transference_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found transference request with id'
                   f'{transference_request_id}'
        )

    if get_patient_transference_by_transference_request_id(
        transference_request_id=transference_request_id,
        db=db
    ) is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'There is already a patient transference for transference'
                   f' request with id {transference_request_id}'
        )

    patient_transference_to_db = PatientTransference.from_orm(
        patient_transference)

    patient_transference_to_db.transference_request_id = transference_request_id

    db.add(patient_transference_to_db)
    db.commit()
    db.refresh(patient_transference_to_db)

    return patient_transference_to_db


def get_all_patient_transferences(db: Session) -> list[PatientTransferenceRead]:
    return db.exec(select(PatientTransference)).all()


def get_patient_transference_by_id(
        id: int, db: Session) -> PatientTransferenceReadDenormalized:

    patient_transference = db.get(PatientTransference, id)

    if not patient_transference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found patient transference with id {id}'
        )

    return patient_transference


def get_patient_transference_by_transference_request_id(
    transference_request_id: int,
    db: Session
) -> PatientTransferenceReadDenormalized:

    return db.exec(
        select(PatientTransference)
        .where(
            and_(
                col(PatientTransference.transference_request_id).is_not(None),
                col(PatientTransference.transference_request_id) == transference_request_id
            )
        )
    ).first()


def get_patient_transference_of_transference_request(
    transference_request_id: int,
    db: Session
) -> PatientTransferenceReadDenormalized:

    transference_request_repository.get_transference_request_by_id(
        id=transference_request_id, db=db)

    # patient_transference = get_patient_transference_by_transference_request_id(
    #     transference_request_id=transference_request_id,
    #     db=db
    # )

    # if not patient_transference:
    #     raise HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f'Transference request with id {transference_request_id}'
    #                f' does not have patient transference yet'
    #     )

    patient_transference = get_patient_transference_by_transference_request_id(
        transference_request_id=transference_request_id,
        db=db
    )

    if not patient_transference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Transference request with id {transference_request_id}'
                   f' does not have patient transference yet'
        )

    return patient_transference


def delete_patient_transference_by_id(id: int, db: Session):
    patient_transference = db.get(PatientTransference, id)

    if not patient_transference:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found patient transference with id {id}'
        )

    db.delete(patient_transference)
    db.commit()
