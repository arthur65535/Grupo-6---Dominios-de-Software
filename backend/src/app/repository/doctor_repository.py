from fastapi import HTTPException, status
from sqlmodel import col, join, select, Session

from app.models.doctor import (
    Doctor,
    DoctorCreate,
    DoctorRead,
    DoctorReadWithMedicalSpecialties
)
from app.models.medical_specialty import MedicalSpecialtyRead
from app.repository import hospital_repository, medical_specialty_repository


def create_doctor(doctor: DoctorCreate, db: Session) -> DoctorRead:
    doctor_to_db = Doctor.from_orm(doctor)

    db.add(doctor_to_db)
    db.commit()
    db.refresh(doctor_to_db)

    return doctor_to_db


def link_doctor_to_hospital(
        doctor_id: int,
        hospital_id: int,
        db: Session
):
    doctor = get_doctor_by_id(id=doctor_id, db=db)
    hospital = hospital_repository.get_hospital_by_id(id=hospital_id, db=db)

    if not doctor:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found doctor with id {doctor_id}'
        )

    if not hospital:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found hospital with id {hospital_id}'
        )

    hospital.doctors.append(doctor)
    db.commit()


def get_all_doctors(db: Session) -> list[DoctorRead]:
    return db.exec(select(Doctor)).all()


def get_doctor_by_id(id: int, db: Session) -> DoctorReadWithMedicalSpecialties:
    doctor = db.get(Doctor, id)

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found doctor with id {id}'
        )

    return doctor


def get_doctors_of_hospital(
        hospital_id: int, db: Session
) -> list[DoctorReadWithMedicalSpecialties]:

    hospital = hospital_repository.get_hospital_by_id(hospital_id, db)

    return hospital.doctors


def get_doctor_by_crm_and_state(
    CRM: str,
    state: str,
    db: Session
) -> DoctorRead:
    doctor = db.exec(
        select(Doctor)
        .where(col(Doctor.CRM) == CRM, col(Doctor.state) == state)
    )

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found doctor with CRM {CRM} in {state}'
        )

    return doctor


def link_medical_specialty_to_doctor(
    medical_specialty_id: int,
    doctor_id: int,
    db: Session
):

    doctor = get_doctor_by_id(id=doctor_id, db=db)
    medical_specialty = medical_specialty_repository \
        .get_medical_specialty_by_id(id=medical_specialty_id, db=db)

    if not doctor:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found doctor with id {doctor_id}'
        )

    if not medical_specialty:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found medical specialty with id'
                   f'{medical_specialty_id}'
        )

    medical_specialty.doctors.append(doctor)
    db.commit()


def get_medical_specialties_of_doctor(
        doctor_id: int, db: Session) -> list[MedicalSpecialtyRead]:

    doctor = get_doctor_by_id(id=doctor_id, db=db)

    return doctor.medical_specialties


def delete_doctor_by_id(id: int, db: Session):
    doctor = db.exec(select(Doctor).where(Doctor.id == id)).first()

    if not doctor:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Not found doctor with id {id}'
        )

    db.delete(doctor)
    db.commit()
