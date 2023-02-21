import csv
import json

from sqlalchemy import text
from sqlmodel import col, select, Session

from app.db.database import engine
from app.models.hospital import Hospital
from app.models.medical_bed import MedicalBedCreate, MedicalBedStatus


def get_medical_beds_for_hospital(
    hospital_id,
    medical_beds_definitions_filepath: str
) -> list[MedicalBedCreate]:

    medical_beds = get_medical_beds_from_medical_beds_definition_file(
        medical_beds_definition_filepath=medical_beds_definitions_filepath,
        hospital_id=hospital_id
    )

    return medical_beds


def get_medical_beds_from_medical_beds_definition_file(
    medical_beds_definition_filepath: str,
    hospital_id: int
) -> list[MedicalBedCreate]:

    medical_beds: list[MedicalBedCreate] = []

    with open(medical_beds_definition_filepath, mode='r') as f:
        csv_reader = csv.DictReader(f)
        next(csv_reader)  # Skip the header.

        for row in csv_reader:
            for i in range(int(row["quantity"])):
                medical_beds.append(
                    MedicalBedCreate(
                        number=i+1,
                        status=MedicalBedStatus.AVAILABLE,
                        medical_bed_type_id=row["medical_bed_type_id"],
                        hospital_id=hospital_id
                    )
                )
    
    return medical_beds


def get_hospital_id_by_CNES(
    CNES: str,
    db: Session
) -> Hospital:

    # return db.exec(
    #     select(Hospital) \
    #     .where(col(Hospital.CNES) == CNES)
    # ).one()

    return db.execute(
        f"""
        SELECT hospital.id
        FROM hospital
        WHERE hospital."CNES" = '{CNES}'
        """
    ).scalar()


def get_medical_beds() -> list[MedicalBedCreate]:
    medical_beds: list[MedicalBedCreate] = []

    with Session(engine) as db:
        HGG_CNES = "2338734"
        HGG_ID = get_hospital_id_by_CNES(HGG_CNES, db=db)
        HGG_MEDICAL_BEDS_DEFINITIONS_FILEPATH = (
            "./app/db/data/generators/"
            "medical_beds_definitions/medical_beds_for_hgg.csv"
        )

        HUGOL_CNES = "7743068"
        HUGOL_ID = get_hospital_id_by_CNES(HUGOL_CNES, db=db)
        HUGOL_MEDICAL_BEDS_DEFINITIONS_FILEPATH = (
            "./app/db/data/generators/"
            "medical_beds_definitions/medical_beds_for_hugol.csv"
        )

        HUGO_CNES = "7743068"
        HUGO_ID = get_hospital_id_by_CNES(HUGO_CNES, db=db)
        HUGO_MEDICAL_BEDS_DEFINITIONS_FILEPATH = (
            "./app/db/data/generators/"
            "medical_beds_definitions/medical_beds_for_hugo.csv"
        )

        HECAD_CNES = "0965324"
        HECAD_ID = get_hospital_id_by_CNES(HECAD_CNES, db=db)
        HECAD_MEDICAL_BEDS_DEFINITIONS_FILEPATH = (
            "./app/db/data/generators/"
            "medical_beds_definitions/medical_beds_for_hecad.csv"
        )

        HC_UFG_CNES = "2338424"
        HC_UFG_ID = get_hospital_id_by_CNES(HC_UFG_CNES, db=db)
        HC_UFG__MEDICAL_BEDS_DEFINITIONS_FILEPATH = (
            "./app/db/data/generators/"
            "medical_beds_definitions/medical_beds_for_hc_ufg.csv"
        )

    medical_beds.extend(get_medical_beds_for_hospital(
        hospital_id=HGG_ID,
        medical_beds_definitions_filepath=HGG_MEDICAL_BEDS_DEFINITIONS_FILEPATH,
    ))

    medical_beds.extend(get_medical_beds_for_hospital(
        hospital_id=HUGO_ID,
        medical_beds_definitions_filepath=HUGO_MEDICAL_BEDS_DEFINITIONS_FILEPATH,
    ))

    medical_beds.extend(get_medical_beds_for_hospital(
        hospital_id=HUGOL_ID,
        medical_beds_definitions_filepath=HUGOL_MEDICAL_BEDS_DEFINITIONS_FILEPATH,
    ))

    medical_beds.extend(get_medical_beds_for_hospital(
        hospital_id=HECAD_ID,
        medical_beds_definitions_filepath=HECAD_MEDICAL_BEDS_DEFINITIONS_FILEPATH,
    ))

    medical_beds.extend(get_medical_beds_for_hospital(
        hospital_id=HC_UFG_ID,
        medical_beds_definitions_filepath=HC_UFG__MEDICAL_BEDS_DEFINITIONS_FILEPATH,
    ))

    return medical_beds


def export_medical_beds_to_json(medical_beds: list[MedicalBedCreate], filepath: str):
    with open(filepath, mode='w') as f:
        json.dump(
            [medical_bed.__dict__ for medical_bed in medical_beds],
            f,
            indent=4,
            default=str
        )


def generate_medical_beds():
    medical_beds = get_medical_beds()

    export_medical_beds_to_json(
        medical_beds=medical_beds,
        filepath="./app/db/data/medical_beds.json"
    )
