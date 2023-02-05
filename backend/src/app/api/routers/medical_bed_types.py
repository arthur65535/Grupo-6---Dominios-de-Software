from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.models.medical_bed_type import MedicalBedTypeCreate, MedicalBedTypeRead
from app.repository import medical_bed_type_repository

router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_medical_bed_type(
    medical_bed_type: MedicalBedTypeCreate, db: Session = Depends(get_session)
) -> MedicalBedTypeRead:
    return medical_bed_type_repository.create_medical_bed_type(
        medical_bed_type=medical_bed_type, db=db
    )


@router.get("/{id}")
def get_medical_bed_type_by_id(
    id: int, db: Session = Depends(get_session)
) -> MedicalBedTypeRead:
    return medical_bed_type_repository.get_medical_bed_type_by_id(id=id, db=db)


@router.get("/")
def get_all_medical_bed_types(
    db: Session = Depends(get_session),
) -> list[MedicalBedTypeRead]:
    return medical_bed_type_repository.get_all_medical_bed_types(db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_bed_type_by_id(id: int, db: Session = Depends(get_session)):
    medical_bed_type_repository.delete_medical_bed_type_by_id(id=id, db=db)
