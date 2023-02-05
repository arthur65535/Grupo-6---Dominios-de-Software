import datetime

from sqlmodel import SQLModel, Field, Relationship


# from app.models.medical_bed import MedicalBedRed


class HospitalBase(SQLModel):
    name: str
    address: str


class Hospital(HospitalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    medical_beds: list["MedicalBed"] = Relationship(back_populates="hospital")


class HospitalCreate(HospitalBase):
    pass


class HospitalRead(HospitalBase):
    id: int


class HospitalReadWithMedicalBeds(HospitalRead):
    medical_beds: list["MedicalBedReadWithMedicalBedType"] = []
