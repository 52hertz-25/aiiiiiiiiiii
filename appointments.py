from fastapi import APIRouter, HTTPException
import sqlite3
from app.db import get_conn
from app.schemas import ApptIn

router = APIRouter()

@router.get("/")
def list_appts():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM appointment").fetchall()
    conn.close()
    return rows

@router.post("/")
def create_appt(a: ApptIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO appointment(patient_id, doctor_id, appt_time, status, note) VALUES (?, ?, ?, ?, ?)",
        (a.patient_id, a.doctor_id, a.appt_time, a.status, a.note)
    )
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, **a.dict()}

@router.put("/{aid}")
def update_appt(aid: int, a: ApptIn):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE appointment SET patient_id=?, doctor_id=?, appt_time=?, status=?, note=? WHERE id=?",
        (a.patient_id, a.doctor_id, a.appt_time, a.status, a.note, aid)
    )
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"id": aid, **a.dict()}

@router.delete("/{aid}")
def delete_appt(aid: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM appointment WHERE id=?", (aid,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Appointment not found")
    return {"message": "Appointment deleted"}
