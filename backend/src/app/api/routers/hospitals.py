from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.models.doctor import DoctorReadWithMedicalSpecialties
from app.models.hospital import (
    HospitalCreate,
    HospitalRead,
    HospitalReadWithMedicalBedsAndDoctors
)
from app.models.medical_bed import (
    MedicalBedCreate,
    MedicalBedRead,
    MedicalBedReadWithMedicalBedType,
)
from app.models.medical_specialty import MedicalSpecialty
from app.repository import (
    hospital_repository,
    medical_bed_repository,
    doctor_repository
)

HospitalReadWithMedicalBedsAndDoctors.update_forward_refs(
    MedicalBedReadWithMedicalBedType=MedicalBedReadWithMedicalBedType
)
DoctorReadWithMedicalSpecialties.update_forward_refs(
    MedicalSpecialty=MedicalSpecialty
)


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_hospital(
    hospital: HospitalCreate, db: Session = Depends(get_session)
) -> HospitalRead:
    return hospital_repository.create_hospital(hospital=hospital, db=db)


@router.get("/")
def get_all_hospitals(
    db: Session = Depends(get_session)
) -> list[HospitalReadWithMedicalBedsAndDoctors]:

    return hospital_repository.get_all_hospitals(db=db)


@router.get("/{id}")
def get_hospital_by_id(
    id: int, db:
    Session = Depends(get_session)
) -> HospitalReadWithMedicalBedsAndDoctors:
    return hospital_repository.get_hospital_by_id(id=id, db=db)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_hospital_by_id(id: int, db: Session = Depends(get_session)):
    hospital_repository.delete_hospital_by_id(id=id, db=db)


@router.post("/{hospital_id}/medical-beds", status_code=status.HTTP_201_CREATED)
def create_medical_bed_for_hospital(
    hospital_id: int, medical_bed: MedicalBedCreate, db: Session = Depends(get_session)
) -> MedicalBedRead:
    return medical_bed_repository.create_medical_bed_for_hospital(
        hospital_id=hospital_id, medical_bed=medical_bed, db=db
    )


@router.put('/{hospital_id}/doctors/{doctor_id}', status_code=status.HTTP_204_NO_CONTENT)
def link_doctor_to_hospital(
        hospital_id: int,
        doctor_id: int,
        db: Session = Depends(get_session)
):

    doctor_repository.link_doctor_to_hospital(
        doctor_id, hospital_id, db)


@router.get('/{hospital_id}/doctors/')
def get_doctors_of_hospital(
    hospital_id,
    db: Session = Depends(get_session)
) -> list[DoctorReadWithMedicalSpecialties]:

    return doctor_repository.get_doctors_of_hospital(hospital_id, db)