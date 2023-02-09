from fastapi import HTTPException, status
from sqlmodel import select, Session

from app.models.patient import (
    Patient,
    PatientCreate,
    PatientRead
)


def create_patient(patient: PatientCreate, db: Session) -> PatientRead:
    patient_to_db = Patient.from_orm(patient)

    db.add(patient_to_db)
    db.commit()
    db.refresh(patient_to_db)

    return patient_to_db


def get_all_patients(db: Session) -> list[Patient]:
    return db.exec(select(Patient)).all()


def get_patient_by_id(id: int, db: Session) -> PatientRead:
    patient = db.get(Patient, id)

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found patient with id {id}'
        )

    return patient


def delete_patient_by_id(id: int, db: Session):
    patient = db.get(Patient, id)

    if not patient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found patient with id {id}'
        )

    db.delete(patient)
    db.commit()

