from fastapi import APIRouter, HTTPException
from app.db import get_conn
from app.schemas import HospIn

router = APIRouter()

@router.get("/")
def list_hosps():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM hospitalization").fetchall()
    conn.close()
    return rows

@router.post("/")
def create_hosp(h: HospIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO hospitalization(patient_id, doctor_id, admit_time, discharge_time, ward, bed_no, status, note) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
        (h.patient_id, h.doctor_id, h.admit_time, h.discharge_time, h.ward, h.bed_no, h.status, h.note)
    )
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, **h.dict()}

@router.put("/{hid}")
def update_hosp(hid: int, h: HospIn):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE hospitalization SET patient_id=?, doctor_id=?, admit_time=?, discharge_time=?, ward=?, bed_no=?, status=?, note=? WHERE id=?",
        (h.patient_id, h.doctor_id, h.admit_time, h.discharge_time, h.ward, h.bed_no, h.status, h.note, hid)
    )
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Hospitalization not found")
    return {"id": hid, **h.dict()}

@router.delete("/{hid}")
def delete_hosp(hid: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM hospitalization WHERE id=?", (hid,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Hospitalization not found")
    return {"message": "Hospitalization deleted"}
