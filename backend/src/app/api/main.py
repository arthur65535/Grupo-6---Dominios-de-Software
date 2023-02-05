import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.responses import FileResponse

from app.api.routers import hospitals, medical_bed_types, medical_beds


def start():
    """Launched with `poetry run start` at root level"""
    uvicorn.run("app.api.main:app", host="0.0.0.0", port=8000, reload=True)


app = FastAPI(
    title="Sistema de Transferência de Pacientes (STP)", version="0.0.1", docs_url=None
)

FAVICON_PATH = "favicon.ico"


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


app.include_router(hospitals.router, prefix="/hospitals")
app.include_router(medical_beds.router, prefix="/medical-beds")
app.include_router(medical_bed_types.router, prefix="/medical-bed-types")


@app.get("/")
def read_root():
    return {"hello": "world"}
