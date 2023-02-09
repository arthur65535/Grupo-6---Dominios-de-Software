
from fastapi import HTTPException, status
from sqlmodel import col, join, select, Session

from app.models.emd_doctor import (
    EMDDoctor,
    EMDDoctorCreate,
    EMDDoctorRead,
)


def create_emd_doctor(emd_doctor: EMDDoctorCreate, db: Session) -> EMDDoctorRead:
    emd_doctor_to_db = EMDDoctor.from_orm(emd_doctor)

    db.add(emd_doctor_to_db)
    db.commit()
    db.refresh(emd_doctor_to_db)

    return emd_doctor_to_db


def get_all_emd_doctors(db: Session) -> list[EMDDoctorRead]:
    return db.exec(select(EMDDoctor)).all()


def get_emd_doctor_by_id(id: int, db: Session) -> EMDDoctorRead:
    emd_doctor = db.get(EMDDoctor, id)

    if not emd_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found emd doctor with id {id}'
        )

    return emd_doctor


def delete_emd_doctor_by_id(id: int, db: Session):
    emd_doctor = db.get(EMDDoctor, id)

    if not emd_doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found emd doctor with id {id}'
        )

    db.delete(emd_doctor)
    db.commit()
