from app.db.data.generators import (
    doctors_generator,
    hospitals_generator,
    medical_bed_types_generator,
    medical_beds_generator,
    patients_generator
)

from app.db.data.insert_predefined_data import insert_hospitals


def generate():
    hospitals_generator.generate_hospitals()

    # It is necessary to insert hospitals to the database since their
    # ids will be fetched via their CNES in the function which
    # generates medical beds.
    insert_hospitals(
        predefined_data_filepath="./app/db/data")

    medical_bed_types_generator.generate_medical_bed_types()
    medical_beds_generator.generate_medical_beds()
    patients_generator.generate_patients(number_of_patients=30)
    doctors_generator.generate_doctors(number_of_doctors_by_hospital=30)
