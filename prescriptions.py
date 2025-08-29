from fastapi import APIRouter, HTTPException
from app.db import get_conn
from app.schemas import PrescriptionIn

router = APIRouter()

@router.get("/")
def list_prescriptions():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM prescription").fetchall()
    conn.close()
    return rows

@router.post("/")
def create_rx(p: PrescriptionIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO prescription(case_id, drug_name, dosage, freq, duration, note) VALUES (?, ?, ?, ?, ?, ?)",
        (p.case_id, p.drug_name, p.dosage, p.freq, p.duration, p.note)
    )
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, **p.dict()}

@router.put("/{pid}")
def update_rx(pid: int, p: PrescriptionIn):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE prescription SET case_id=?, drug_name=?, dosage=?, freq=?, duration=?, note=? WHERE id=?",
        (p.case_id, p.drug_name, p.dosage, p.freq, p.duration, p.note, pid)
    )
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return {"id": pid, **p.dict()}

@router.delete("/{pid}")
def delete_rx(pid: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM prescription WHERE id=?", (pid,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Prescription not found")
    return {"message": "Prescription deleted"}
