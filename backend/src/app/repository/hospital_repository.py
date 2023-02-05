from fastapi import HTTPException, status
from sqlmodel import select, Session

from app.models.hospital import (
    Hospital,
    HospitalCreate,
    HospitalRead,
    HospitalReadWithMedicalBeds,
)


def create_hospital(hospital: HospitalCreate, db: Session) -> HospitalRead:
    hospital_to_db = Hospital.from_orm(hospital)

    db.add(hospital_to_db)
    db.commit()
    db.refresh(hospital_to_db)

    return hospital_to_db


def get_all_hospitals(db: Session) -> list[HospitalReadWithMedicalBeds]:
    return db.exec(select(Hospital)).all()


def get_hospital_by_id(id: int, db: Session) -> HospitalReadWithMedicalBeds:
    hospital = db.exec(select(Hospital).where(Hospital.id == id)).first()

    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {id}",
        )

    return hospital


def exist_hospital_with_id(id: int, db: Session) -> bool:
    return db.get(Hospital, id)


def delete_hospital_by_id(id: int, db: Session):
    hospital = db.exec(select(Hospital).where(Hospital.id == id)).first()

    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {id}",
        )

    db.delete(hospital)
    db.commit()
