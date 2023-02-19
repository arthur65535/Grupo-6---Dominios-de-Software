from sqlmodel import select, Session, SQLModel

from app.db.database import engine
from app.models.doctor import Doctor
from app.models.doctor_hospital_link import DoctorHospitalLink
from app.models.doctor_medical_specialty_link import DoctorMedicalSpecialtyLink
from app.models.emd_doctor import EMDDoctor
from app.models.hospital import Hospital
from app.models.medical_bed import MedicalBed
from app.models.medical_bed_type import MedicalBedType
from app.models.medical_specialty import MedicalSpecialty
from app.models.patient import Patient
from app.models.patient_clinical_condition import PatientClinicalCondition
from app.models.patient_transference import PatientTransference
from app.models.transference_request import TransferenceRequest
from app.models.update_of_patient_clinical_condition import \
    UpdateOfPatientClinicalCondition


def delete():
    models: list[SQLModel] = [
        MedicalBed,
        MedicalBedType,
        PatientTransference,
        PatientClinicalCondition,
        UpdateOfPatientClinicalCondition,
        TransferenceRequest,
        EMDDoctor,
        Hospital,
        DoctorHospitalLink,
        DoctorMedicalSpecialtyLink,
        Doctor,
        MedicalSpecialty,
        Patient,
    ]

    with Session(engine) as session:
        for model in models:
            delete_statement = select(model)
            rows = session.exec(delete_statement).all()
            for row in rows:
                session.delete(row)

        session.commit()
