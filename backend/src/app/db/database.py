import json
import random

from sqlmodel import Session, SQLModel, create_engine

from app.models.doctor import *
from app.models.emd_doctor import *
from app.models.hospital import *
from app.models.medical_bed import *
from app.models.medical_bed_type import *
from app.models.medical_specialty import *
from app.models.patient import *
from app.models.transference_request import *

from app.repository import doctor_repository, hospital_repository

from sqlalchemy.exc import IntegrityError
from psycopg2.errors import UniqueViolation

USER = "postgres"
PASSWORD = 123456789
HOST = "localhost"
PORT = 5432
DATABASE = "stp"

CONNECTION_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(CONNECTION_URL, echo=False)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


def insert_predefined_data():
    with Session(engine) as session:
        PREDEFINED_DATA_FILEPATH = './app/db/data'
        print(f"\nAdding predefined data in '{PREDEFINED_DATA_FILEPATH}'\n")

        insert_medical_specialties(PREDEFINED_DATA_FILEPATH, session)
        insert_hospitals(PREDEFINED_DATA_FILEPATH, session)
        insert_patients(PREDEFINED_DATA_FILEPATH, session)
        insert_doctors(PREDEFINED_DATA_FILEPATH, session)
        link_doctors_to_hospital(max_number_of_doctors_by_hospital=5, db=session)


def insert_medical_specialties(predefined_data_filepath: str, db: Session):
    with open(
        f"{predefined_data_filepath}/medical_specialties.json",
        mode="r"
    ) as f:
        print("Adding medical specialties.\n")
        medical_specialties_defined_by_cfm = json.load(f)

        for medical_specialty_dict in medical_specialties_defined_by_cfm:
            try:
                medical_specialty_db = MedicalSpecialty(
                    **medical_specialty_dict
                )
                db.add(medical_specialty_db)
                db.commit()
                db.refresh(medical_specialty_db)
                print(f"Medical specialty '{medical_specialty_dict['name']}'"
                      f" with id {medical_specialty_dict['id']} added.")
            except IntegrityError as error:
                if '(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "medical_specialty_pkey"' in str(error):
                    print(f"Medical specialty '{medical_specialty_dict['name']}'"
                          f" with id {medical_specialty_dict['id']} already"
                          f" added previously.")
                    db.rollback()
                else:
                    raise error
        print("\nMedical specialties specialties added.\n")


def insert_hospitals(predefined_data_filepath: str, db: Session):
    with open(
        f"{predefined_data_filepath}/hospitals.json",
        mode="r"
    ) as f:
        print("Adding hospitals.\n")
        hospitals = json.load(f)

        for hospital in hospitals:
            try:
                hospital_db = Hospital(
                    **hospital
                )
                hospital_db.management = hospital["management"].split(".")[1]
                hospital_db.management_type = hospital["management_type"].split(".")[1]
                db.add(hospital_db)
                db.commit()
                db.refresh(hospital_db)
                print(f"Hospital named '{hospital['name']}'"
                      f" with CNES {hospital['CNES']} added.")
            except IntegrityError as error:
                if 'already exists' in str(error):
                    print(f"Hospital named '{hospital['name']}'"
                          f" with CNES {hospital['CNES']} already"
                          f" added previously.")
                    db.rollback()
                else:
                    raise error
        print("\nHospitals added.\n")


def insert_patients(predefined_data_filepath: str, db: Session):
    with open(
        f"{predefined_data_filepath}/patients.json",
        mode="r"
    ) as f:
        print("Adding patients.\n")
        patients = json.load(f)

        for patient in patients:
            try:
                patient_db = Patient(
                    **patient
                )
                db.add(patient_db)
                db.commit()
                db.refresh(patient_db)
                print(f"Fake Patient named '{patient['name']}'"
                      f" with CPF {patient['CPF']} added.")
            except IntegrityError as error:
                if 'already exists' in str(error):
                    print(f"Fake Patient named '{patient['name']}'"
                          f" with CPF {patient['CPF']} already"
                          f" added previously.")
                    db.rollback()
                else:
                    raise error
        print("\nPatients added.\n")


def insert_doctors(predefined_data_filepath: str, db: Session):
    with open(
        f"{predefined_data_filepath}/doctors.json",
        mode="r"
    ) as f:
        print("Adding doctors.\n")
        doctors = json.load(f)

        for doctor in doctors:
            try:
                doctor_db = Doctor(
                    **doctor
                )
                db.add(doctor_db)
                db.commit()
                db.refresh(doctor_db)
                print(f"Fake Doctor named '{doctor['name']}'"
                      f" with CRM {doctor['CRM']} added.")
            except IntegrityError as error:
                if 'already exists' in str(error):
                    print(f"Fake Doctor named '{doctor['name']}'"
                          f" with CRM {doctor['CRM']} already"
                          f" added previously.")
                    db.rollback()
                else:
                    raise error
        print("\nDoctors added.\n")


def link_doctors_to_hospital(max_number_of_doctors_by_hospital: int, db: Session):
    all_doctors = doctor_repository.get_all_doctors(db=db)
    all_hospitals = hospital_repository.get_all_hospitals(db=db)

    print("Linking doctors to hospitals.\n")

    for doctor in all_doctors:
        hospital_id = random.choice(all_hospitals).id

        doctors_already_linked_to_hospital = \
            doctor_repository.get_doctors_of_hospital(hospital_id, db)

        if len(doctors_already_linked_to_hospital) \
            + 1 > max_number_of_doctors_by_hospital:
            break
    
        if doctor.id in [doctor.id for doctor in doctors_already_linked_to_hospital]:
            break
        

        doctor_repository.link_doctor_to_hospital(
            doctor_id=doctor.id,
            hospital_id=hospital_id,
            db=db
        )

        print(f"Doctor with id {doctor.id} linked to hospital with id"
              f" {hospital_id}")


    print("\nDoctors linked to hospitals.\n")