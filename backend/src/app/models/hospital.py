import datetime
import enum

from sqlmodel import SQLModel, Field, Relationship

from app.models.doctor import Doctor, DoctorReadWithMedicalSpecialties
from app.models.doctor_hospital_link import DoctorHospitalLink


class HospitalManagement(enum.Enum):
    ESTADUAL = "estadual"
    MUNICIPAL = "municipal"
    DUPLA = "dupla"


class HospitalManagementType(enum.Enum):
    ADMINISTRACAL_PUBLICA = "Administração pública"
    ENTIDADES_EMPRESARIAIS = "Entidades empresariais"
    ENTIDADES_SEM_FINS_LUCRATIVOS = "Entidades sem fins lucrativos"
    ORGANIZACOES_INTERNACIONAIS_OUTRAS = "Organizações internacionais/outras"
    PESSOAS_FISICAS = "Pessoas físicas"


class HospitalBase(SQLModel):
    name: str
    initials: str
    address: str
    CNES: str = Field(unique=True)
    phone_number_1: str
    phone_number_2: str | None = Field(nullable=True)
    is_active: bool
    CNPJ: str = Field(unique=True)
    email_address: str
    management: HospitalManagement
    management_type: HospitalManagementType


class Hospital(HospitalBase, table=True):
    id: int | None = Field(default=None, primary_key=True)

    medical_beds: list["MedicalBed"] = Relationship(back_populates="hospital")

    doctors: list[Doctor] = Relationship(
        back_populates='hospitals',
        link_model=DoctorHospitalLink
    )

    transference_requests: list['TransferenceRequest'] = Relationship(
        back_populates='requesting_hospital')

    incoming_transferences: list['PatientTransference'] = Relationship(
        back_populates='destination_hospital')


class HospitalCreate(HospitalBase):
    pass


class HospitalRead(HospitalBase):
    id: int


class HospitalReadWithMedicalBedsAndDoctors(HospitalRead):
    medical_beds: list['MedicalBedReadWithMedicalBedType'] = []
    doctors: list[DoctorReadWithMedicalSpecialties] = []
