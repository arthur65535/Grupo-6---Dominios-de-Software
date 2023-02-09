import datetime
from typing import Optional

from sqlalchemy.orm import RelationshipProperty
from sqlmodel import Field, Relationship, SQLModel

from app.models.doctor import Doctor
from app.models.hospital import Hospital
from app.models.patient import Patient
from app.models.medical_bed_type import MedicalBedType


class TransferenceRequestBase(SQLModel):
    solicitation_datetime: datetime.datetime
    rationale: str

    patient_id: int | None = Field(
        default=None, foreign_key='patient.id', nullable=False)

    requesting_doctor_id: int | None = Field(
        default=None, foreign_key='doctor.id', nullable=False)

    requesting_hospital_id: int | None = Field(
        default=None, foreign_key='hospital.id', nullable=False)

    medical_bed_type_id: int | None = Field(
        default=None, foreign_key='medical_bed_type.id', nullable=False)

    patient_transference_id: int | None = Field(
        default=None,
        foreign_key='patient_transference.id',
        nullable=True,
        unique=True
    )


class TransferenceRequest(TransferenceRequestBase, table=True):
    __tablename__ = 'transference_request'

    id: int | None = Field(default=None, primary_key=True)

    patient: Patient | None = Relationship(
        back_populates='transference_requests')

    requesting_doctor: Doctor | None = Relationship(
        back_populates='transference_requests')

    requesting_hospital: Hospital | None = Relationship(
        back_populates='transference_requests')

    medical_bed_type: MedicalBedType | None = Relationship(
        back_populates='transference_requests')

    # patient_transference: 'PatientTransference' | None = Relationship(
    #     back_populates='transference_request')

    patient_transference: Optional['PatientTransference'] = Relationship(
        back_populates='transference_request',
        sa_relationship=RelationshipProperty(
            'patient_transference',
            primaryjoin='foreign(transference_request.id) == patient_transference.transference_request_id',
            uselist=False
        )
    )


class TransferenceRequestCreate(TransferenceRequestBase):
    pass


class TransferenceRequestRead(TransferenceRequestBase):
    id: int


class TransferenceRequestReadDenormalized(TransferenceRequestRead):
    patient: Patient
    requesting_doctor: Doctor
    requesting_hospital: Hospital
    medical_bed_type: MedicalBedType
    patient_transference: Optional['PatientTransference']
