from fastapi import HTTPException, status
from sqlmodel import Session, col, select

from app.models.medical_bed_type import (
    MedicalBedType,
    MedicalBedTypeCreate,
    MedicalBedTypeRead,
)


def create_medical_bed_type(
    medical_bed_type: MedicalBedTypeCreate, db: Session
) -> MedicalBedTypeRead:
    medical_bed_type_to_db = MedicalBedType.from_orm(medical_bed_type)

    if exists_medical_bed_type_with_name(medical_bed_type.name, db):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"There is already a medical bed type named"
            f" {medical_bed_type.name}",
        )

    db.add(medical_bed_type_to_db)
    db.commit()
    db.refresh(medical_bed_type_to_db)

    return medical_bed_type_to_db


def get_all_medical_bed_types(db: Session) -> list[MedicalBedTypeRead]:
    return db.exec(select(MedicalBedType)).all()


def get_medical_bed_type_by_id(id: int, db: Session) -> MedicalBedTypeRead:
    medical_bed_type = db.get(MedicalBedType, id)

    if not medical_bed_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed type with id {id}",
        )

    return medical_bed_type


def get_medical_bed_type_by_name(name: str, db: Session) -> MedicalBedTypeRead:
    medical_bed_type = db.exec(
        select(MedicalBedType).where(col(MedicalBedType.name) == name)
    ).first()

    if not medical_bed_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed type named {name}",
        )

    return medical_bed_type


def delete_medical_bed_type_by_id(id: int, db: Session):
    medical_bed_type = db.get(MedicalBedType, id)

    if not medical_bed_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed type with id {id}",
        )

    db.delete()
    db.commit()


def exists_medical_bed_type_with_name(name: str, db: Session) -> bool:
    return db.exec(
        select(MedicalBedType).where(col(MedicalBedType.name) == name)
    ).first()


def exists_medical_bed_type_with_id(id: int, db: Session) -> bool:
    return db.get(MedicalBedType, id)


def delete_medical_bed_type_by_id(name: str, db: Session):
    medical_bed_type = db.exec(
        select(MedicalBedType).where(col(MedicalBedType.name) == name)
    ).first()

    if not medical_bed_type:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found medical bed type named {name}",
        )

    db.delete(medical_bed_type)
    db.commit()
