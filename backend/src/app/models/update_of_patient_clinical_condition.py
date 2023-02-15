import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel


class UpdateOfPatientClinicalConditionBase(SQLModel):
    datetime_of_update: datetime.datetime
    description: str

    patient_clinical_condition_id: int | None = Field(
        default=None,
        foreign_key="patient_clinical_condition.id",
        nullable=False,
    )


class UpdateOfPatientClinicalCondition(UpdateOfPatientClinicalConditionBase, table=True):
    __tablename__ = 'update_of_patient_clinical_condition'

    id: int | None = Field(default=None, primary_key=True)

    patient_clinical_condition: Optional["PatientClinicalCondition"] \
        = Relationship(back_populates="updates_of_patient_clinical_condition")


class UpdateOfPatientClinicalConditionCreate(UpdateOfPatientClinicalConditionBase):
    pass


class UpdateOfPatientClinicalConditionRead(UpdateOfPatientClinicalConditionBase):
    id: int
