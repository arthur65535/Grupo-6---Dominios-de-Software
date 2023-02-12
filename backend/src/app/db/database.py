import json

from sqlmodel import Session, SQLModel, create_engine

from app.models.doctor import *
from app.models.emd_doctor import *
from app.models.hospital import *
from app.models.medical_bed import *
from app.models.medical_bed_type import *
from app.models.medical_specialty import *
from app.models.patient import *
from app.models.transference_request import *

from sqlalchemy.exc import IntegrityError


USER = "postgres"
PASSWORD = 123456789
HOST = "localhost"
PORT = 5432
DATABASE = "stp"

CONNECTION_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
engine = create_engine(CONNECTION_URL, echo=True)


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
                print(f"Medical specialty '{medical_specialty_dict['name']}'"
                      f" with id {medical_specialty_dict['id']} added.")
            except IntegrityError as error:
                if '(psycopg2.errors.UniqueViolation) duplicate key value violates unique constraint "medical_specialty_pkey' in str(error):
                    print(f"Medical specialty '{medical_specialty_dict['name']}'"
                          f" with id {medical_specialty_dict['id']} already"
                          f" added previously.")
                    db.rollback()
                else:
                    raise error
        print("\nMedical specialties specialties added.\n")
