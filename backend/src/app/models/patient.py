import datetime

from sqlmodel import SQLModel, Field, Relationship


class PatientBase(SQLModel):
    name: str | None = Field(index=True)
    birth_date: datetime.date | None
    gender: str
    address: str | None = None


class Patient(PatientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    transference_requests: list["TransferenceRequest"] = Relationship(
        back_populates="patient"
    )


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int
