import datetime

from sqlmodel import SQLModel, Field, Relationship

from app.models.doctor_medical_specialty_link import DoctorMedicalSpecialtyLink
from app.models.doctor_hospital_link import DoctorHospitalLink


class DoctorBase(SQLModel):
    name: str
    state: str
    CRM: str
    birth_date: datetime.date
    gender: str
    address: str


class Doctor(DoctorBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    medical_specialties: list["MedicalSpecialty"] = Relationship(
        back_populates="doctors", link_model=DoctorMedicalSpecialtyLink
    )

    transference_requests: list["TransferenceRequest"] = Relationship(
        back_populates="requesting_doctor"
    )

    hospitals: list['Hospital'] = Relationship(
        back_populates='doctors', link_model=DoctorHospitalLink)


class DoctorCreate(DoctorBase):
    pass


class DoctorRead(DoctorBase):
    id: int


class DoctorReadWithMedicalSpecialties(DoctorRead):
    medical_specialties: list['MedicalSpecialty'] = []
