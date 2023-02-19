import uvicorn
from fastapi import Depends, FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse

from app.db.data.generators import generate_predefined_data
from app.db.data import insert_predefined_data, delete_predefined_data

from app.api.routers import (
    doctors,
    emd_doctors,
    hospitals,
    medical_bed_types,
    medical_beds,
    medical_specialties,
    patient_clinical_conditions,
    patients,
    patient_transferences,
    transference_requests
)


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)


app = FastAPI(
    title="Sistema de Transferência de Pacientes (STP)", version="0.0.1", docs_url=None
)

FAVICON_PATH = "favicon.ico"

@app.on_event('startup')
def on_startup():
    delete_predefined_data.delete()
    generate_predefined_data.generate()
    insert_predefined_data.insert()


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    return FileResponse(FAVICON_PATH)


@app.get("/docs", include_in_schema=False)
def swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url="openapi.json",
        title="Sistema de Transferência de Pacientes (STP)",
        swagger_favicon_url="/favicon.ico",
    )


app.include_router(doctors.router, prefix='/doctors')
app.include_router(emd_doctors.router, prefix='/emd-doctors')
app.include_router(hospitals.router, prefix='/hospitals')
app.include_router(medical_beds.router, prefix='/medical-beds')
app.include_router(medical_bed_types.router, prefix='/medical-bed-types')
app.include_router(medical_specialties.router, prefix='/medical-specialties')
app.include_router(
    patient_clinical_conditions.router,
    prefix='/patient-clinical-conditions'
)
app.include_router(patients.router, prefix='/patients')
app.include_router(
    patient_transferences.router, prefix='/patient-transferences'
)
app.include_router(
    transference_requests.router, prefix='/transference-requests'
)


@app.get("/")
def read_root():
    return {"hello": "world"}
