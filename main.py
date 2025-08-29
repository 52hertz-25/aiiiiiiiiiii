from fastapi import FastAPI
from app.db import init_db
from app.routers import (
    patients, doctors, appointments, case_records, prescriptions, hospitalizations
)

app = FastAPI()

# 项目启动时初始化数据库
init_db()

app.include_router(patients.router, prefix="/patients", tags=["Patients"])
app.include_router(doctors.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointments.router, prefix="/appointments", tags=["Appointments"])
app.include_router(case_records.router, prefix="/case_records", tags=["Case Records"])
app.include_router(prescriptions.router, prefix="/prescriptions", tags=["Prescriptions"])
app.include_router(hospitalizations.router, prefix="/hospitalizations", tags=["Hospitalizations"])
