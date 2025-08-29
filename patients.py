from fastapi import APIRouter
from ..db import get_conn
from ..schemas import PatientIn

router = APIRouter(prefix="/patients", tags=["Patients"])

@router.get("/")
def list_patients():
    with get_conn() as conn:
        rows = conn.execute("SELECT * FROM patient").fetchall()
    return [dict(r) for r in rows]

@router.post("/")
def create_patient(p: PatientIn):
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO patient(name, gender, age, phone, id_number, address) VALUES (?, ?, ?, ?, ?, ?)",
            (p.name, p.gender, p.age, p.phone, p.id_number, p.address)
        )
        pid = cur.lastrowid
    return {"id": pid, **p.dict()}

@router.put("/{pid}")
def update_patient(pid: int, p: PatientIn):
    with get_conn() as conn:
        conn.execute(
            "UPDATE patient SET name=?, gender=?, age=?, phone=?, id_number=?, address=? WHERE id=?",
            (p.name, p.gender, p.age, p.phone, p.id_number, p.address, pid)
        )
    return {"id": pid, **p.dict()}

@router.delete("/{pid}")
def delete_patient(pid: int):
    with get_conn() as conn:
        conn.execute("DELETE FROM patient WHERE id=?", (pid,))
    return {"status": "deleted", "id": pid}

