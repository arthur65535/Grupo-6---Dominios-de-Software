import datetime

from sqlmodel import Field, Relationship, SQLModel

from app.models.doctor import Doctor
from app.models.emd_doctor import EMDDoctor
from app.models.patient import Patient
from app.models.medical_bed_type import MedicalBedType


class TransferenceRequestBase(SQLModel):
    solicitation_datetime: datetime.datetime
    rationale: str

    patient_id: int | None = Field(
        default=None, foreign_key="patient.id", nullable=False
    )

    requesting_doctor_id: int | None = Field(
        default=None, foreign_key="doctor.id", nullable=False
    )

    emd_doctor_id: int | None = Field(
        default=None, foreign_key="emd_doctor.id", nullable=False
    )

    medical_bed_type_id: int | None = Field(
        default=None, foreign_key="medical_bed_type.id", nullable=False
    )


class TransferenceRequest(TransferenceRequestBase, table=True):
    __tablename__ = "transference_request"

    id: int | None = Field(default=None, primary_key=True)

    patient: Patient | None = Relationship(back_populates="transference_requests")
    requesting_doctor: Doctor | None = Relationship(
        back_populates="transference_requests"
    )
    emd_doctor: EMDDoctor | None = Relationship(back_populates="transference_requests")
    medical_bed_type: MedicalBedType | None = Relationship(
        back_populates="transference_requests"
    )


class TransferenceRequestCreate(TransferenceRequestBase):
    pass


class TransferenceRequestRead(TransferenceRequestBase):
    id: int
