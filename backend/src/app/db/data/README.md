## Dados pré-definidos

Este diretório contém dados pré-definidos que serão inseridos no banco de dados automaticamente pelo Web Service sempre que este for iniciado.


### Dados pré-definidos reais

Até o momento, há os seguintes dados **reais** pré-definidos:

- Especialidades Médicas definidas pela Resolução nº 2.221/2018 do Conselho Federal de Medicina. Nome do arquivo `medical_specialties.json`

- Hospitais: dados de 5 hospitais de Goiânia, sendo eles:
  - HGG.
  - HUGO.
  - HUGOL.
  - HC-UFG.
  - HECAD.

  Nome do arquivo: `hospitals.json`.

- Tipos de Leitos Médicos: dados dos tipos de leitos de leitos médicos presentes nos hospitais citados acima. Nome do arquivo: `medical_bed_types.json`.

- Leitos Médicos: dados dos leitos médicos dosdos hospitais supracitados. As definições de quais dados serão gerados estão no arquivo `generators/medical_beds_definitions` e os dados em si, no arquivo `medical_beds.json`.


### Dados pré-definidos fakes

Além disso, há também os seguintes dados **fakes**:

- Médicos: dados de médicos. A inserção desses dados também vincula alguns médicos a alguns hospitais. Nome do arquivo: `doctors.json`.

- Pacientes: dados pessoais de pacientes. Nome do arquivo: `patients.json`.


### Fontes dos dados

Os dados reais sobre os hospitais e seus leitos foram coletados do [Conselho Nacional de Estabelecimentos de Saúde (CNES)](https://cnes.datasus.gov.br/).

Os dados reais sobre especialidades médicas foram extraídos da [resolução do CFM mencionada](https://sistemas.cfm.org.br/normas/visualizar/resolucoes/BR/2018/2221).

Já os dados fakes são gerados automaticamente utilizando a biblioteca em Python [Faker](https://faker.readthedocs.io/en/master/).
