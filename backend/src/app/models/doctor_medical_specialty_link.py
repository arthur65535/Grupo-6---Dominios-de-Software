import datetime

from sqlmodel import SQLModel, Field, Relationship


class DoctorMedicalSpecialtyLink(SQLModel, table=True):
    __tablename__ = "doctor_medical_specialty_link"

    doctor: int | None = Field(default=None, foreign_key="doctor.id", primary_key=True)

    medical_specialty: int | None = Field(
        default=None, foreign_key="medical_specialty.id", primary_key=True
    )
