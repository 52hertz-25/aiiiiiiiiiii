from fastapi import APIRouter, HTTPException
from app.db import get_conn
from app.schemas import CaseIn

router = APIRouter()

@router.get("/")
def list_cases():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM case_record").fetchall()
    conn.close()
    return rows

@router.post("/")
def create_case(c: CaseIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO case_record(patient_id, doctor_id, visit_time, diagnosis, symptoms, treatment) VALUES (?, ?, ?, ?, ?, ?)",
        (c.patient_id, c.doctor_id, c.visit_time, c.diagnosis, c.symptoms, c.treatment)
    )
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, **c.dict()}

@router.put("/{cid}")
def update_case(cid: int, c: CaseIn):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE case_record SET patient_id=?, doctor_id=?, visit_time=?, diagnosis=?, symptoms=?, treatment=? WHERE id=?",
        (c.patient_id, c.doctor_id, c.visit_time, c.diagnosis, c.symptoms, c.treatment, cid)
    )
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Case record not found")
    return {"id": cid, **c.dict()}

@router.delete("/{cid}")
def delete_case(cid: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM case_record WHERE id=?", (cid,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Case record not found")
    return {"message": "Case record deleted"}
