from pydantic import BaseModel
from typing import Optional

# 患者
class PatientIn(BaseModel):
    name: str
    gender: str
    age: int
    phone: Optional[str] = None
    id_number: Optional[str] = None
    address: Optional[str] = None

# 医生
class DoctorIn(BaseModel):
    name: str
    department: str
    title: Optional[str] = None
    phone: Optional[str] = None

# 预约
class ApptIn(BaseModel):
    patient_id: int
    doctor_id: int
    appt_time: str
    status: Optional[str] = "scheduled"
    note: Optional[str] = None

# 病例
class CaseIn(BaseModel):
    patient_id: int
    doctor_id: int
    visit_time: str
    diagnosis: Optional[str] = None
    symptoms: Optional[str] = None
    treatment: Optional[str] = None

# 处方
class PrescriptionIn(BaseModel):
    case_id: int
    drug_name: str
    dose: Optional[str] = None
    tid: Optional[str] = None
    days: Optional[int] = None
    note: Optional[str] = None

# 住院
class HospIn(BaseModel):
    patient_id: int
    doctor_id: int
    admit_time: str
    discharge_time: Optional[str] = None
    ward: Optional[str] = None
    bed_no: Optional[str] = None
    status: Optional[str] = "admitted"
    note: Optional[str] = None
