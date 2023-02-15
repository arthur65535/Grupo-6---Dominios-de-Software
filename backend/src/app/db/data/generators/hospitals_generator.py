import json

from faker import Faker

from app.models.hospital import (
    HospitalCreate,
    HospitalManagement,
    HospitalManagementType
)

fake = Faker(locale="pt_BR")


def get_hospitals() -> list[HospitalCreate]:
    hospitals: list[HospitalCreate] = []

    hospitals.append(HospitalCreate(
        name="Hospital Estadual Geral de Goiânia Dr. Alberto Rassi",
        initials="HGG",
        address="Avenida Anhanguera nº 6.479, Setor Oeste, Goiânia - GO, CEP: 74.110-010",
        CNES="2338734",
        phone_number_1="(62) 3209-9800",
        is_active=True,
        CNPJ="02.529.964/0004-42",
        email_address="contato@idtech.org.br",
        management=HospitalManagement.ESTADUAL,
        management_type=HospitalManagementType.ADMINISTRACAL_PUBLICA
    ))

    hospitals.append(HospitalCreate(
        name="Hospital Estadual de Urgências Governador Otávio Lage de Siqueira",
        initials="HUGOL",
        address="Av. Anhanguera, 14527 – St. Santos Dumont, Goiânia – GO, 74463-350",
        CNES="7743068",
        phone_number_1="(62) 3270-6300",
        is_active=True,
        CNPJ="05.029.600/0003-68",
        email_address="hugol@hugol.org.br",
        management=HospitalManagement.ESTADUAL,
        management_type=HospitalManagementType.ADMINISTRACAL_PUBLICA
    ))

    hospitals.append(HospitalCreate(
        name="Hospital Estadual de Urgências de Goiás – Dr.Valdemiro Cruz",
        initials="HUGO",
        address="Avenida 31 de Março, s/n – São Pedro Ludovico, Goiânia – GO, 74820-300",
        CNES="2338262",
        phone_number_1="(62) 3201-4420",
        is_active=True,
        CNPJ="02.529.964/0008-23",
        email_address="atendimento@hugo.org.br",
        management=HospitalManagement.ESTADUAL,
        management_type=HospitalManagementType.ADMINISTRACAL_PUBLICA
    ))

    hospitals.append(HospitalCreate(
        name="Hospital Estadual da Criança e do Adolescente",
        initials="Hecad",
        address="Av. Bela Vista, 2.333 - Parque Acalanto. Goiânia - Goiás CEP: 74863-025",
        CNES="0965324",
        phone_number_1="(62) 3142-5757",
        is_active=True,
        CNPJ="05.029.600/0009-53",
        email_address="hecad.nir@gmail.com",
        management=HospitalManagement.ESTADUAL,
        management_type=HospitalManagementType.ADMINISTRACAL_PUBLICA
    ))


    return hospitals


def export_hospitals_to_json(hospitals: list[HospitalCreate], filepath: str):
    with open(filepath, mode='w') as f:
        # hospital_dicts = [hospital.__dict__ for hospital in hospitals]

        # for hospital_dict in hospital_dicts:
        #     hospital_dict['management'] = hospital_dict['management'].value
        #     hospital_dict['management_type'] = hospital_dict['management_type'].value

        # json.dump(
        #     hospital_dicts,
        #     f,
        #     indent=4,
        #     default=str
        # )
        json.dump(
            [hospital.__dict__ for hospital in hospitals],
            f,
            indent=4,
            default=str
        )


def generate_hospitals():
    hospitals = get_hospitals()
    export_hospitals_to_json(hospitals, filepath="./app/db/data/hospitals.json")

