import datetime

from sqlmodel import SQLModel, Field, Relationship

from app.models.doctor import Doctor, DoctorReadWithMedicalSpecialties
from app.models.doctor_hospital_link import DoctorHospitalLink


class HospitalBase(SQLModel):
    name: str
    address: str


class Hospital(HospitalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    medical_beds: list["MedicalBed"] = Relationship(back_populates="hospital")

    doctors: list[Doctor] = Relationship(
        back_populates='hospitals',
        link_model=DoctorHospitalLink
    )

    transference_requests: list['TransferenceRequest'] = Relationship(
        back_populates='requesting_hospital')

    incoming_transferences: list['PatientTransference'] = Relationship(
        back_populates='destination_hospital')


class HospitalCreate(HospitalBase):
    pass


class HospitalRead(HospitalBase):
    id: int


class HospitalReadWithMedicalBedsAndDoctors(HospitalRead):
    medical_beds: list['MedicalBedReadWithMedicalBedType'] = []
    doctors: list[DoctorReadWithMedicalSpecialties] = []
