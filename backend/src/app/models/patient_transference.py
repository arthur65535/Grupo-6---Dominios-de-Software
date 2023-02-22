import datetime
import enum

from sqlalchemy.orm import RelationshipProperty
from sqlmodel import Field, Relationship, SQLModel

from app.models.doctor import Doctor, DoctorReadWithMedicalSpecialties
from app.models.emd_doctor import EMDDoctor, EMDDoctorRead
from app.models.hospital import Hospital, HospitalRead
from app.models.transference_request import TransferenceRequest


class PatientTransferenceStatus(enum.Enum):
    AUTHORIZED = 'authorized'
    IN_TRANSIT = 'in_transit'
    COMPLETED = 'completed'


class PatientTransferenceBase(SQLModel):
    authorization_datetime: datetime.datetime
    in_transit_datetime: datetime.datetime | None
    completed_datetime: datetime.datetime | None
    status: PatientTransferenceStatus

    transference_request_id: int | None = Field(
        default=None,
        foreign_key='transference_request.id',
        nullable=False,
        unique=True
    )

    emd_doctor_id: int | None = Field(
        default=None, foreign_key='emd_doctor.id', nullable=False)

    destination_hospital_id: int | None = Field(
        default=None, foreign_key='hospital.id', nullable=False)

    receiving_doctor_id: int | None = Field(
        default=None, foreign_key='doctor.id', nullable=False)


class PatientTransference(PatientTransferenceBase, table=True):
    __tablename__ = 'patient_transference'

    id: int | None = Field(default=None, primary_key=True)

    # transference_request: TransferenceRequest | None = Relationship(
    #     back_populates='patient_transference', 
    #     sa_relationship=RelationshipProperty(
    #         'transference_request',
    #         primaryjoin='foreign(patient_transference.id) == transference_request.patient_transference_id',
    #         uselist=False
    #     )
    # )

    transference_request: TransferenceRequest | None = Relationship(
        back_populates='patient_transference')

    emd_doctor: EMDDoctor | None = Relationship(
        back_populates='patient_transferences')

    destination_hospital: Hospital | None = Relationship(
        back_populates='incoming_transferences')

    receiving_doctor: Doctor | None = Relationship(
        back_populates='received_transferences')


class PatientTransferenceCreate(PatientTransferenceBase):
    pass


class PatientTransferenceRead(PatientTransferenceBase):
    id: int


class PatientTransferenceReadDenormalized(PatientTransferenceRead):
    emd_doctor: EMDDoctorRead
    destination_hospital: HospitalRead
    receiving_doctor: DoctorReadWithMedicalSpecialties
