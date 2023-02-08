import datetime

from sqlmodel import SQLModel, Field, Relationship


class EMDDoctorBase(SQLModel):
    name: str
    state: str
    CRM: str
    birth_date: datetime.date
    gender: str
    address: str


class EMDDoctor(EMDDoctorBase, table=True):
    __tablename__ = "emd_doctor"

    id: int | None = Field(default=None, primary_key=True)

    transference_requests: list["TransferenceRequest"] = Relationship(
        back_populates="emd_doctor"
    )


class EMDDoctorCreate(EMDDoctorBase):
    pass


class EMDDoctorRead(EMDDoctorBase):
    id: int
