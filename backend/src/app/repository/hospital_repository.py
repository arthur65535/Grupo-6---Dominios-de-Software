from fastapi import HTTPException, status
from sqlmodel import col, select, Session

from app.models.hospital import (
    Hospital,
    HospitalCreate,
    HospitalRead,
    HospitalReadWithMedicalBedsAndDoctors
)


def create_hospital(hospital: HospitalCreate, db: Session) -> HospitalRead:
    hospital_to_db = Hospital.from_orm(hospital)

    db.add(hospital_to_db)
    db.commit()
    db.refresh(hospital_to_db)

    return HospitalRead.from_orm(hospital_to_db)


def get_all_hospitals(db: Session) -> list[HospitalReadWithMedicalBedsAndDoctors]:
    return db.exec(select(Hospital)).all()


def get_hospital_by_id(id: int, db: Session) -> HospitalReadWithMedicalBedsAndDoctors:
    hospital = db.get(Hospital, id)

    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {id}",
        )

    return hospital




def exist_hospital_with_id(pk_id: int, db: Session) -> bool:
    hospital = db.get(Hospital, pk_id)
    return bool(hospital)


def delete_hospital_by_id(pk_id: int, db: Session):
    hospital = db.get(Hospital, pk_id)

    if not hospital:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {pk_id}",
        )

    db.delete(hospital)
    db.commit()
