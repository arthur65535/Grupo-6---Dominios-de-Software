from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.doctor import DoctorCreate, DoctorReadWithMedicalSpecialties
from app.models.medical_specialty import MedicalSpecialtyRead
from app.repository import doctor_repository


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_doctor(
    doctor: DoctorCreate,
    db: Session = Depends(get_session)
) -> DoctorReadWithMedicalSpecialties:

    return doctor_repository.create_doctor(doctor=doctor, db=db)


@router.get('/')
def get_all_doctors(
        db: Session = Depends(get_session)
) -> list[DoctorReadWithMedicalSpecialties]:

    return doctor_repository.get_all_doctors(db=db)


@router.get('/{id}')
def get_doctor_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> DoctorReadWithMedicalSpecialties:

    return doctor_repository.get_doctor_by_id(id=id, db=db)


@router.get('/')
def get_all_doctors(
    db: Session = Depends(get_session)
) -> list[DoctorReadWithMedicalSpecialties]:

    return doctor_repository.get_all_doctors(db=db)


@router.put('/{doctor_id}/medical-specialties/{medical_specialty_id}',
            status_code=status.HTTP_204_NO_CONTENT)
def link_medical_specialty_to_doctor(
        doctor_id: int,
        medical_specialty_id: int,
        db: Session = Depends(get_session)
):

    doctor_repository.link_medical_specialty_to_doctor(
        medical_specialty_id, doctor_id, db)


@router.get('/{doctor_id}/medical-specialties/')
def get_medical_specialties_of_doctor(
    doctor_id: int,
    db: Session = Depends(get_session)
) -> list[MedicalSpecialtyRead]:
    
    return doctor_repository.get_medical_specialties_of_doctor(
        doctor_id=doctor_id, db=db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_doctor_by_id(id: int, db: Session = Depends(get_session)):
    doctor_repository.delete_doctor_by_id(id=id, db=db)
