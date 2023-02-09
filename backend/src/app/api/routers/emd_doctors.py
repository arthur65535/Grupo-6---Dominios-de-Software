from fastapi import APIRouter, status, Depends
from sqlmodel import Session

from app.db.database import get_session
from app.models.emd_doctor import EMDDoctor, EMDDoctorCreate, EMDDoctorRead
from app.models.patient_transference import PatientTransference
from app.repository import emd_doctor_repository


EMDDoctor.update_forward_refs(
    PatientTransference=PatientTransference
)


router = APIRouter()


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_emd_doctor(
    emd_doctor: EMDDoctorCreate,
    db: Session = Depends(get_session)
) -> EMDDoctorRead:

    return emd_doctor_repository.create_emd_doctor(
        emd_doctor=emd_doctor, db=db)


@router.get('/')
def get_all_emd_doctors(
        db: Session = Depends(get_session)
) -> list[EMDDoctorRead]:

    return emd_doctor_repository.get_all_emd_doctors(db=db)


@router.get('/{id}')
def get_emd_doctor_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> EMDDoctorRead:

    return emd_doctor_repository.get_emd_doctor_by_id(id=id, db=db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_emd_doctor_by_id(id: int, db: Session = Depends(get_session)):
    emd_doctor_repository.delete_emd_doctor_by_id(id=id, db=db)
