from fastapi import Depends, HTTPException, status
from sqlmodel import Session, col, select

from app.db.database import get_session
from app.models.medical_bed import (
    MedicalBed,
    MedicalBedCreate,
    MedicalBedReadWithMedicalBedType,
)
from app.repository import hospital_repository, medical_bed_type_repository


def create_medical_bed_for_hospital(
    hospital_id: int, medical_bed: MedicalBedCreate, db: Session = Depends(get_session)
) -> MedicalBedReadWithMedicalBedType:
    if not hospital_repository.get_hospital_by_id(id=hospital_id, db=db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {id} to add medical bed",
        )

    medical_bed_to_db = MedicalBed.from_orm(medical_bed)
    medical_bed_to_db.hospital_id = hospital_id

    db.add(medical_bed_to_db)
    db.commit()
    db.refresh(medical_bed_to_db)

    return medical_bed_to_db


def get_all_medical_beds(
    db: Session = Depends(get_session),
) -> list[MedicalBedReadWithMedicalBedType]:
    return db.exec(select(MedicalBed)).all()


def get_all_medical_beds_of_given_type(
    medical_bed_type_id: int, db: Session = Depends(get_session)
) -> list[MedicalBedReadWithMedicalBedType]:
    if not medical_bed_type_repository.get_medical_bed_type_by_id(
        id=medical_bed_type_id, db=db
    ):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed type with id {medical_bed_type_id}",
        )

    return db.exec(
        select(MedicalBed).where(
            col(MedicalBed.medical_bed_type_id) == medical_bed_type_id
        )
    ).all()


def get_medical_beds_of_hospital(
    hospital_id: int, db: Session
) -> list[MedicalBedReadWithMedicalBedType]:
    if not hospital_repository.get_hospital_by_id(id=hospital_id, db=db):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found hospital with id {hospital_id}",
        )

    return db.exec(
        select(MedicalBed).where(col(MedicalBed.hospital_id) == hospital_id)
    ).all()


def get_medical_bed_by_id(id: int, db: Session) -> MedicalBedReadWithMedicalBedType:
    medical_bed = db.exec(select(MedicalBed).where(MedicalBed.id == id)).first()

    if not medical_bed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed with id {id}",
        )

    return medical_bed


def delete_medical_bed_by_id(id: int, db: Session):
    medical_bed = db.get(MedicalBed, id)

    if not medical_bed:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed with id {id}",
        )

    db.delete(medical_bed)
    db.commit()
