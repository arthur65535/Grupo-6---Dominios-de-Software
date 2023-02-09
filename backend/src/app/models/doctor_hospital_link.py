import datetime

from sqlmodel import SQLModel, Field


class DoctorHospitalLink(SQLModel, table=True):
    __tablename__ = 'doctor_hospital_link'

    doctor: int | None = Field(
        default=None, foreign_key='doctor.id', primary_key=True)

    hospital: int | None = Field(
        default=None, foreign_key='hospital.id', primary_key=True)
