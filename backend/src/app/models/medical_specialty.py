import datetime

from sqlmodel import SQLModel, Field, Relationship

from app.models.doctor import Doctor
from app.models.doctor_medical_specialty_link import DoctorMedicalSpecialtyLink


class MedicalSpecialtyBase(SQLModel):
    id: int
    name: str = Field(unique=True, index=True)
    description: str | None = None


class MedicalSpecialty(MedicalSpecialtyBase, table=True):
    __tablename__ = "medical_specialty"

    id: int | None = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": False}
    )

    doctors: list[Doctor] = Relationship(
        back_populates="medical_specialties", link_model=DoctorMedicalSpecialtyLink
    )


class MedicalSpecialtyCreate(MedicalSpecialtyBase):
    pass


class MedicalSpecialtyRead(MedicalSpecialtyBase):
    pass
