from fastapi import HTTPException, status

from sqlmodel import select, Session

from app.models.patient_clinical_condition import (
    PatientClinicalCondition,
    PatientClinicalConditionCreate,
    PatientClinicalConditionRead,
    PatientClinicalConditionReadWithUpdates
)
from app.models.update_of_patient_clinical_condition import (
    UpdateOfPatientClinicalCondition,
    UpdateOfPatientClinicalConditionCreate,
    UpdateOfPatientClinicalConditionRead
)
from app.repository import transference_request_repository


def create_patient_clinical_condition(
    patient_clinical_condition: PatientClinicalConditionCreate,
    db: Session
) -> PatientClinicalConditionReadWithUpdates:

    # if not transference_request_repository.exists_transference_request_with_id(
    #     id=patient_clinical_condition.transference_request_id,
    #     db=db
    # ):
    #     return HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f'Not found transference request with id'
    #                f'{patient_clinical_condition.transference_request_id}'
    #     )

    transference_request = transference_request_repository \
        .get_transference_request_by_id(
            patient_clinical_condition.transference_request_id,
            db
        )

    if transference_request.patient_clinical_condition is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f'There is already a clinical condition for transference'
                   f' request with id {transference_request.id}'
        )

    patient_clinical_condition_to_db = PatientClinicalCondition.from_orm(
        patient_clinical_condition)

    db.add(patient_clinical_condition_to_db)
    db.commit()
    db.refresh(patient_clinical_condition_to_db)

    return patient_clinical_condition_to_db


def get_all_patient_clinical_conditions(
    db: Session
) -> list[PatientClinicalConditionReadWithUpdates]:

    return db.exec(select(PatientClinicalCondition)).all()


def get_patient_clinical_condition_by_id(
    id: int,
    db: Session
) -> PatientClinicalConditionReadWithUpdates:

    patient_clinical_condition = db.get(PatientClinicalCondition, id)

    if not patient_clinical_condition:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Not found patient clinical condition with id {id}"
        )

    return patient_clinical_condition


# def create_update_of_patient_clinical_condition(
#     update_of_patient_clinical_condition: UpdateOfPatientClinicalConditionCreate,
#     db: Session
# ):
#     patient_clinical_condition = update_of_patient_clinical_condition.


def get_clinical_condition_by_transference_request_id(
    transference_request_id: int,
    db: Session
) -> PatientClinicalConditionReadWithUpdates:

    # if not transference_request_repository.exists_transference_request_with_id(
    #     id=transference_request_id,
    #     db=db
    # ):
    #     return HTTPException(
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         detail=f"Not found transference request with id"
    #                f"{transference_request_id}"
    #     )

    transference_request = transference_request_repository \
        .get_transference_request_by_id(
            id=transference_request_id,
            db=db
        )

    return transference_request.patient_clinical_condition


def create_update_of_patient_clinical_condition(
    patient_clinical_condition_id: int,
    update_of_patient_clinical_condition: UpdateOfPatientClinicalConditionCreate,
    db: Session
) -> UpdateOfPatientClinicalConditionRead:

    patient_clinical_condition = get_patient_clinical_condition_by_id(
        id=patient_clinical_condition_id,
        db=db
    )

    update_of_patient_clinical_condition_to_db \
        = UpdateOfPatientClinicalCondition.from_orm(
            update_of_patient_clinical_condition
        )

    db.add(update_of_patient_clinical_condition_to_db)
    db.commit()
    db.refresh(update_of_patient_clinical_condition_to_db)

    patient_clinical_condition.updates_of_patient_clinical_condition.append(
        update_of_patient_clinical_condition_to_db
    )

    db.commit()

    return update_of_patient_clinical_condition_to_db


def get_updates_of_patient_clinical_condition(
    patient_clinical_condition_id: int,
    db: Session
) -> list[UpdateOfPatientClinicalConditionRead]:

    patient_clinical_condition = get_patient_clinical_condition_by_id(
        id=patient_clinical_condition_id,
        db=db
    )

    return patient_clinical_condition.updates_of_patient_clinical_condition
