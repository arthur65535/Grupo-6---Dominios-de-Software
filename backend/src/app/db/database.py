from sqlmodel import Session, SQLModel, create_engine

from app.models.doctor import *
from app.models.emd_doctor import *
from app.models.hospital import *
from app.models.medical_bed import *
from app.models.medical_bed_type import *
from app.models.medical_specialty import *
from app.models.patient import *
from app.models.transference_request import *

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
