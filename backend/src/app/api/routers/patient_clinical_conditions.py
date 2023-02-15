from fastapi import APIRouter, Depends, status
from sqlmodel import Session

from app.db.database import get_session
from app.models.patient_clinical_condition import (
    PatientClinicalCondition,
    PatientClinicalConditionCreate,
    PatientClinicalConditionRead,
    PatientClinicalConditionReadWithUpdates
)
from app.models.transference_request import TransferenceRequest
from app.models.update_of_patient_clinical_condition import (
    UpdateOfPatientClinicalCondition,
    UpdateOfPatientClinicalConditionCreate,
    UpdateOfPatientClinicalConditionRead
)
from app.repository import patient_clinical_condition_repository


PatientClinicalCondition.update_forward_refs(
    TransferenceRequest=TransferenceRequest
)
UpdateOfPatientClinicalCondition.update_forward_refs(
    PatientClinicalCondition=PatientClinicalCondition
)


router = APIRouter()


@router.get("/")
def get_all_patient_clinical_conditions(
    db: Session = Depends(get_session)
) -> list[PatientClinicalConditionReadWithUpdates]:

    return patient_clinical_condition_repository \
        .get_all_patient_clinical_conditions(db=db)


@router.get("/{id}")
def get_patient_clinical_condition_by_id(
    id: int,
    db: Session = Depends(get_session)
) -> PatientClinicalConditionReadWithUpdates:

    return patient_clinical_condition_repository \
        .get_patient_clinical_condition_by_id(id=id, db=db)


@router.post(
    "/{patient_clinical_condition_id}/updates-of-patient-clinical-condition",
    status_code=status.HTTP_201_CREATED
)
def create_update_of_patient_clinical_condition(
    patient_clinical_condition_id: int,
    update_of_patient_clinial_condition: UpdateOfPatientClinicalConditionCreate,
    db: Session = Depends(get_session)
):

    return patient_clinical_condition_repository \
        .create_update_of_patient_clinical_condition(
            update_of_patient_clinial_condition,
            db
        )


@router.get(
    "/{patient_clinical_condition_id}/updates-of-patient-clinical-condition",
)
def get_updates_of_patient_clinical_condition(
    patient_clinical_condition_id: int,
    db: Session = Depends(get_session)
):

    return patient_clinical_condition_repository \
        .get_updates_of_patient_clinical_condition(
            patient_clinical_condition_id,
            db=db
        )
