from fastapi import HTTPException, status
from sqlmodel import Session, col, select

from app.models.medical_specialty import (
    MedicalSpecialty,
    MedicalSpecialtyCreate,
    MedicalSpecialtyRead
)


def create_medical_specialty(
    medical_specialty: MedicalSpecialtyCreate,
    db: Session
) -> MedicalSpecialtyRead:

    medical_specialty_to_db = MedicalSpecialty.from_orm(medical_specialty)

    if exists_medical_specialty_with_name(medical_specialty.name, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'There is already a medical speciaty named'
                   f' {medical_specialty.name}'
        )

    db.add(medical_specialty_to_db)
    db.commit()
    db.refresh(medical_specialty_to_db)

    return medical_specialty_to_db


def get_all_medical_specialties(db: Session) -> list[MedicalSpecialtyRead]:
    return db.exec(select(MedicalSpecialty)).all()


def get_medical_specialty_by_id(id: int, db: Session) -> MedicalSpecialty:
    medical_specialty = db.get(MedicalSpecialty, id)

    if not medical_specialty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found medical specialty with id {id}'
        )

    return medical_specialty


def get_medical_specialty_by_name(name: str, db: Session) -> MedicalSpecialty:
    medical_specialty = db.exec(
        select(MedicalSpecialty)
        .where(col(MedicalSpecialty.name) == name)
    ).first()

    if not medical_specialty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found medical specialty named {name}'
        )

    return medical_specialty 


def delete_medical_specialty_by_id(id: int, db: Session):
    medical_specialty = db.get(MedicalSpecialty, id)

    if not medical_specialty:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found medical specialty with id {id}'
        )

    db.delete(medical_specialty)
    db.commit()


def exists_medical_specialty_with_name(name: str, db: Session) -> bool:
    return db.exec(
        select(MedicalSpecialty)
        .where(col(MedicalSpecialty.name) == name)
    ).first()


def exists_medical_specialty_id(id: int, db: Session) -> bool:
    return db.get(MedicalSpecialty, id)
