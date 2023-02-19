import datetime
import enum

from sqlmodel import SQLModel, Field, Relationship, UniqueConstraint

from app.models.hospital import Hospital
from app.models.medical_bed_type import MedicalBedType


class MedicalBedStatus(enum.Enum):
    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"


class MedicalBedBase(SQLModel):
    __table_args__ = (
        UniqueConstraint("number", "medical_bed_type_id", "hospital_id"),
    )

    number: int
    status: MedicalBedStatus = Field(default=MedicalBedStatus.AVAILABLE)

    medical_bed_type_id: int | None = Field(
        default=None, foreign_key="medical_bed_type.id", nullable=False
    )

    hospital_id: int | None = Field(
        default=None, foreign_key="hospital.id", nullable=False
    )


class MedicalBed(MedicalBedBase, table=True):
    __tablename__ = "medical_bed"

    id: int | None = Field(default=None, primary_key=True)

    medical_bed_type: MedicalBedType = Relationship(back_populates="medical_beds")
    hospital: Hospital = Relationship(back_populates="medical_beds")


class MedicalBedCreate(MedicalBedBase):
    pass


class MedicalBedRead(MedicalBedBase):
    id: int
    hospital_id: int


class MedicalBedReadWithMedicalBedType(MedicalBedRead):
    medical_bed_type: MedicalBedType
