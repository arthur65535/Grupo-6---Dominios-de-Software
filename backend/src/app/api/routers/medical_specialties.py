from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.medical_specialty import (
    MedicalSpecialtyCreate,
    MedicalSpecialtyRead
)
from app.repository import medical_specialty_repository, doctor_repository


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_medical_specialty(
    medical_specialty: MedicalSpecialtyCreate,
    db: Session = Depends(get_session)
) -> MedicalSpecialtyRead:

    return medical_specialty_repository.create_medical_specialty(
        medical_specialty=medical_specialty, db=db)


@router.get('/')
def get_all_medical_specialties(
        db: Session = Depends(get_session)) -> list[MedicalSpecialtyRead]:

    return medical_specialty_repository.get_all_medical_specialties(db=db)


@router.get('/{id}')
def get_medical_specialty_by_id(
        id: int, db: Session = Depends(get_session)) -> MedicalSpecialtyRead:

    return medical_specialty_repository.get_medical_specialty_by_id(id, db)




@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_medical_specialty_by_id(
        id: int, db: Session = Depends(get_session)):

    medical_specialty_repository.delete_medical_specialty_by_id(id=id, db=db)
