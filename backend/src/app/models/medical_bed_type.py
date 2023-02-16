import datetime
import enum

from sqlmodel import SQLModel, Field, Relationship


class MedicalBedTypeBase(SQLModel):
    id: int
    name: str
    specialty: str


class MedicalBedType(MedicalBedTypeBase, table=True):
    __tablename__ = "medical_bed_type"

    id: int | None = Field(
        default=None, primary_key=True, sa_column_kwargs={"autoincrement": False}
    )

    medical_beds: list["MedicalBed"] = Relationship(back_populates="medical_bed_type")

    transference_requests: list["TransferenceRequest"] = Relationship(
        back_populates="medical_bed_type"
    )


class MedicalBedTypeCreate(MedicalBedTypeBase):
    pass


class MedicalBedTypeRead(MedicalBedTypeBase):
    pass
