from app.db.data.generators import (
    doctors_generator,
    hospitals_generator,
    medical_bed_types_generator,
    patients_generator
)

def generate():
    hospitals_generator.generate_hospitals()
    medical_bed_types_generator.generate_medical_bed_types()
    patients_generator.generate_patients(number_of_patients=30)
    doctors_generator.generate_doctors(number_of_doctors_by_hospital=30)
