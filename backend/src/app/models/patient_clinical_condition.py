import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel

from app.models.update_of_patient_clinical_condition import \
    UpdateOfPatientClinicalCondition


class PatientClinicalConditionBase(SQLModel):
    heart_rate_in_beats_per_minute: int = Field(ge=0)
    respiratory_rate_in_breaths_per_minute: int = Field(ge=0)
    glascow_coma_scale: int = Field(ge=3, le=15)
    clinical_summary: str
    physical_exams: str
    subsidiary_exams: str
    conduct_taken: str

    transference_request_id: int | None = Field(
        default=None,
        foreign_key="transference_request.id",
        nullable=False,
        unique=True
    )


class PatientClinicalCondition(PatientClinicalConditionBase, table=True):
    __tablename__ = "patient_clinical_condition"

    id: int | None = Field(default=None, primary_key=True)

    transference_request: Optional["TransferenceRequest"] = Relationship(
        back_populates="patient_clinical_condition"
    )

    updates_of_patient_clinical_condition: \
        list[UpdateOfPatientClinicalCondition] = Relationship(
            back_populates="patient_clinical_condition"
        )


class PatientClinicalConditionCreate(PatientClinicalConditionBase):
    pass


class PatientClinicalConditionRead(PatientClinicalConditionBase):
    id: int


class PatientClinicalConditionReadWithUpdates(PatientClinicalConditionRead):
    updates_of_patient_clinical_condition: \
        list[UpdateOfPatientClinicalCondition] = []
