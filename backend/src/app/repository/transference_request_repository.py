from fastapi import HTTPException, status
from sqlmodel import select, Session

from app.models.transference_request import (
    TransferenceRequest,
    TransferenceRequestCreate,
    TransferenceRequestRead,
    TransferenceRequestReadDenormalized
)


def create_transference_request(
        transference_request: TransferenceRequestCreate,
        db: Session
) -> TransferenceRequestRead:

    transference_request_to_db = TransferenceRequest.from_orm(
        transference_request)

    db.add(transference_request_to_db)
    db.commit()
    db.refresh(transference_request_to_db)

    return transference_request_to_db


def get_all_transference_requests(
        db: Session) -> list[TransferenceRequestReadDenormalized]:

    return db.exec(select(TransferenceRequest)).all()


def get_transference_request_by_id(
        id: int, db: Session) -> TransferenceRequestReadDenormalized:

    transference_request = db.get(TransferenceRequest, id)

    if not transference_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found transference request with id {id}'
        )

    return transference_request


def delete_transference_request_by_id(id: int, db: Session):
    transference_request = db.get(TransferenceRequest, id)

    if not transference_request:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found transference request with id {id}'
        )

    db.delete(transference_request)
    db.commit()
