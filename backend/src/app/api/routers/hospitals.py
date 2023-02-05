from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.models.hospital import (
    HospitalCreate,
    HospitalRead,
    HospitalReadWithMedicalBeds,
)
from app.models.medical_bed import (
    MedicalBedCreate,
    MedicalBedRead,
    MedicalBedReadWithMedicalBedType,
)
from app.repository import hospital_repository, medical_bed_repository

HospitalReadWithMedicalBeds.update_forward_refs(
    MedicalBedReadWithMedicalBedType=MedicalBedReadWithMedicalBedType
)


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
def create_hospital(
    hospital: HospitalCreate, db: Session = Depends(get_session)
) -> HospitalRead:
    return hospital_repository.create_hospital(hospital=hospital, db=db)


@router.get("/")
def get_all_hospitals(
    db: Session = Depends(get_session),
) -> list[HospitalReadWithMedicalBeds]:
    return hospital_repository.get_all_hospitals(db=db)


@router.get("/{id}")
def get_hospital_by_id(
    id: int, db: Session = Depends(get_session)
) -> HospitalReadWithMedicalBeds:
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
