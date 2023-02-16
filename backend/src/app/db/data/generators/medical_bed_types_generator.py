import json

from app.models.medical_bed_type import MedicalBedTypeCreate


def get_medical_bed_types() -> list[MedicalBedTypeCreate]:
    medical_bed_types: list[MedicalBedTypeCreate] = []

    medical_bed_types.append(MedicalBedTypeCreate(
        id=1,
        name="BUCO MAXILO FACIAL",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=2,
        name="CARDIOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=3,
        name="CIRURGIA GERAL",
        specialty="CIRURGICO",
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=4,
        name="ENDOCRINOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=5,
        name="GASTROENTEROLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=6,
        name="GINECOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=7,
        name="CIRURGICO/DIAGNOSTICO/TERAPEUTICO",
        specialty="HOSPITAL DIA"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=8,
        name="NEFROLOGIAUROLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=9,
        name="NEUROCIRURGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=10,
        name="OBSTETRICIA CIRURGICA",
        specialty="OBSTETRICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=11,
        name="OFTALMOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=12,
        name="ONCOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=13,
        name="ORTOPEDIATRAUMATOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=14,
        name="OTORRINOLARINGOLOGIA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=15,
        name="PLASTICA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=16,
        name="TORACICA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=16,
        name="TORACICA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=16,
        name="TORACICA",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=32,
        name="CARDIOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=33,
        name="CLINICA GERAL",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=34,
        name="CRONICOS",
        specialty="OUTRAS ESPECIALIDADES"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=35,
        name="DERMATOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=36,
        name="GERIATRIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=37,
        name="HANSENOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=38,
        name="HEMATOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=40,
        name="NEFROUROLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=41,
        name="NEONATOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=42,
        name="NEUROLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=43,
        name="OBSTETRICIA CLINICA",
        specialty="OBSTETRICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=44,
        name="ONCOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=45,
        name="PEDIATRIA CLINICA",
        specialty="PEDIATRICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=46,
        name="PNEUMOLOGIA",
        specialty="CLINICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=66,
        name="UNIDADE ISOLAMENTO",
        specialty="COMPLEMENTAR"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=67,
        name="TRANSPLANTE",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=68,
        name="PEDIATRIA CIRURGICA",
        specialty="PEDIATRICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=75,
        name="UTI ADULTO - TIPO II",
        specialty="COMPLEMENTAR"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=78,
        name="UTI PEDIATRICA - TIPO II",
        specialty="COMPLEMENTAR"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=81,
        name="UTI NEONATAL - TIPO II",
        specialty="COMPLEMENTAR"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=83,
        name="UTI DE QUEIMADOS",
        specialty="COMPLEMENTAR"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=90,
        name="QUEIMADO ADULTO",
        specialty="CIRURGICO"
    ))
    medical_bed_types.append(MedicalBedTypeCreate(
        id=91,
        name="QUEIMADO PEDIATRICO",
        specialty="CIRURGICO"
    ))

    return medical_bed_types


def export_medical_bed_types_to_json(medical_bed_types: list[MedicalBedTypeCreate], filepath: str):
    with open(filepath, mode='w') as f:
        json.dump(
            [medical_bed_type.__dict__ for medical_bed_type in medical_bed_types],
            f,
            indent=4,
            default=str
        )


def generate_medical_bed_types():
    medical_bed_types = get_medical_bed_types()
    export_medical_bed_types_to_json(
        medical_bed_types, filepath="./app/db/data/medical_bed_types.json")
