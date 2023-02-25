# Backend do STP

O backend do STP é um Web Service RESTful, isto é, um Web Service com o [estilo arquitetural REST](https://restfulapi.net/).


## Tecnologias

O backendo foi desenvolvindo em Python 3.10 utilizando as seguintes tecnologias:

- FastAPI: Framework Web moderno do Python baseado no Starlette e Pydantic.
- Poetry: Ferramenta de gerenciamento de dependências e build do Python.
- SQLModel: Framework ORM baseado no SQLAlchemy e Pydantic.
- Alembic: Framework de gerenciamento migrations (mudanças no schema do banco de dados).
- PostgreSQL: SGBD relacional.
- Docker: Plataforma utilizada para virtualização a nível de containers.
- Docker Compose: Ferramenta utilizada para definir e executar aplicações com múltiplos containers dockers, no caso do Backend do STP, há um container para o Web Service e um para o SGBD.


## Arquitetura

### Arquitetura lógica da aplicação

A arquitetura lógica do backend está representada pelo diagrama localizado em https://github.com/arthur65535/Grupo-6---Dominios-de-Software/blob/main/Documenta%C3%A7%C3%A3o/ArquiteturaLógicadoBackend.jpg

### Arquitetura física da aplicação

A arquitetura física do backend do STP pretendida envolve os serviços de cloud representados no arquivo em https://github.com/arthur65535/Grupo-6---Dominios-de-Software/blob/main/Documenta%C3%A7%C3%A3o/ArquiteturaFísicadoBackend.png.

Entretanto, devido a restrição de tempo para implementação, a arquitetura física de fato implementada não seguiu a arquitetura projetada. Na realidade, foi utilizado o serviço Amazon EC2 com o armazenamento e processamento reunido nele.

### Arquitetura de dados

A arquitetura de dados escolhida foi um banco de dados relacional como SGBD PostgreSQL.

O diagrama conceitual do schema do banco de dados, contendo seus tipos de entidades e relacionamentos, está no arquivo https://github.com/arthur65535/Grupo-6---Dominios-de-Software/blob/main/Documenta%C3%A7%C3%A3o/DiagramaEntidade-Relacionamento.jpg.


## Instalação

### Pré-requisitos

- Docker.
- Docker Compose.
- Git.

### Passos

1. Clone o repositório do projeto STP:

```sh
git clone https://github.com/arthur65535/Grupo-6---Dominios-de-Software
```

2. Vá até o diretório do backend:

```sh
cd backend
```

3. Use o docker compose para criar os containers e executá-los em background:

```sh
docker compose up -d
```

Pronto, agora é possível verificar que o Web Service está executando utilizando algum cliente HTTP, por exemplo, o curl:

```sh
curl -X GET http://localhost:8000/ --include
```

Tal requisição terá como resposta uma mensagem com status code 200 OK e body contendo o objeto JSON `{"hello": "world"}`


## Documentação

É possível acessar uma documentação interativa do API REST gerada automaticamente pelo Swagger UI na URL `http://localhost:8000/docs` ou pelo ReDoc em `http://localhost:8000/redoc`.

Tais documentações são geradas a partir do conteúdo no arquivo JSON em `http://localhost:8000/openapi.json` baseado no padrão [OpenAPI](https://swagger.io/resources/open-api/).
