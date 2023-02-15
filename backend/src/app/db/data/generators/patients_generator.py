import datetime
import json

from faker import Faker

from app.models.patient import PatientCreate

fake = Faker(locale="pt_BR")


def get_fake_patients(number_of_patients: int, fake: Faker) -> list[PatientCreate]:
    patients: list[PatientCreate] = []

    for i in range(number_of_patients):
        is_even = i % 2 == 0

        patient = PatientCreate(
            name=fake.name_male() if is_even else fake.name_female(),
            birth_date=fake.date_of_birth(),
            gender="M" if is_even else "F",
            CPF=fake.ssn(),
            RG=fake.rg(),
            mother_name=fake.name_female(),
            father_name=fake.name_male(),
            phone_number=fake.cellphone_number(),
            is_deceased=False,
            is_deprived_of_liberty=fake.boolean(chance_of_getting_true=1),
            has_disability=fake.boolean(chance_of_getting_true=15)
        )

        patients.append(patient)

    return patients


def export_patients_to_json(patients: list[PatientCreate], filepath: str):
    with open(filepath, mode='w') as f:
        json.dump(
            [patient.__dict__ for patient in patients],
            f,
            indent=4,
            default=str
        )


def generate_patients(number_of_patients: int):
    patients = get_fake_patients(number_of_patients, fake=fake)
    export_patients_to_json(patients, filepath="./app/db/data/patients.json")
