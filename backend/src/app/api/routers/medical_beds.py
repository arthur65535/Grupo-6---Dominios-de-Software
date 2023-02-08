from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.medical_bed import MedicalBedRead, MedicalBedReadWithMedicalBedType
from app.repository import medical_bed_repository


router = APIRouter()


@router.get("/")
def get_all_medical_beds(
    db: Session = Depends(get_session),
) -> list[MedicalBedReadWithMedicalBedType]:
    return medical_bed_repository.get_all_medical_beds(db=db)


@router.get("/{id}")
def get_medical_bed_by_id(
    id: int, db: Session = Depends(get_session)
) -> MedicalBedRead:
    return medical_bed_repository.get_medical_bed_by_id(id=id, db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_by_id(id: int, db: Session = Depends(get_session)):
    medical_bed_repository.delete_medical_bed_by_id(id=id, db=db)
