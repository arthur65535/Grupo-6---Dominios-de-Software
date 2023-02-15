import datetime

from sqlmodel import SQLModel, Field, Relationship


class PatientBase(SQLModel):
    name: str | None = Field(index=True)
    birth_date: datetime.date | None
    gender: str
    address: str | None = None
    email_address: str | None
    CNS: str | None = Field(unique=True)
    CPF: str | None = Field(unique=True)
    RG: str | None
    mother_name: str | None
    father_name: str | None
    ethnic_group: str | None
    phone_number: str | None
    is_deceased: bool
    is_deprived_of_liberty: bool | None
    has_disability: bool | None
    weight_in_kg: int | None
    height_in_cm: int | None



class Patient(PatientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    transference_requests: list["TransferenceRequest"] = Relationship(
        back_populates="patient"
    )


class PatientCreate(PatientBase):
    pass


class PatientRead(PatientBase):
    id: int
