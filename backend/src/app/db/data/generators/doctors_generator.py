import datetime
import json

from faker import Faker

from app.models.doctor import DoctorCreate
from app.models.hospital import *
from app.repository import hospital_repository

fake = Faker(locale="pt_BR")


def get_fake_doctors(number_of_doctors: int, fake: Faker) -> list[DoctorCreate]:
    doctors: list[DoctorCreate] = []

    for i in range(number_of_doctors):
        is_even = i % 2 == 0

        doctor = DoctorCreate(
            name=fake.name_male() if is_even else fake.name_female(),
            state="GO",
            CRM=fake.ssn()[:5],
            CPF=fake.ssn(),
            RG=fake.ssn()[:7],
            birth_date=fake.date_of_birth(minimum_age=24, maximum_age=75),
            gender="M" if is_even else "F",
            address=fake.address()
        )

        doctors.append(doctor)

    return doctors


def export_doctors_to_json(doctors: list[DoctorCreate], filepath: str):
    with open(filepath, mode='w') as f:
        json.dump(
            [doctor.__dict__ for doctor in doctors],
            f,
            indent=4,
            default=str
        )


def generate_doctors(number_of_doctors_by_hospital: int):
    doctors = get_fake_doctors(number_of_doctors_by_hospital, fake=fake)
    export_doctors_to_json(doctors, filepath="./app/db/data/doctors.json")
