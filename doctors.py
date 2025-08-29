from fastapi import APIRouter, HTTPException
import sqlite3
from app.db import get_conn
from app.schemas import DoctorIn

router = APIRouter()

# 查询所有医生
@router.get("/")
def list_doctors():
    conn = get_conn()
    rows = conn.execute("SELECT * FROM doctor").fetchall()
    conn.close()
    return rows

# 新建医生
@router.post("/")
def create_doctor(d: DoctorIn):
    conn = get_conn()
    cur = conn.execute(
        "INSERT INTO doctor(name, department, title, phone) VALUES (?, ?, ?, ?)",
        (d.name, d.department, d.title, d.phone)
    )
    conn.commit()
    conn.close()
    return {"id": cur.lastrowid, **d.dict()}

# 更新医生
@router.put("/{did}")
def update_doctor(did: int, d: DoctorIn):
    conn = get_conn()
    cur = conn.execute(
        "UPDATE doctor SET name=?, department=?, title=?, phone=? WHERE id=?",
        (d.name, d.department, d.title, d.phone, did)
    )
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"id": did, **d.dict()}

# 删除医生
@router.delete("/{did}")
def delete_doctor(did: int):
    conn = get_conn()
    cur = conn.execute("DELETE FROM doctor WHERE id=?", (did,))
    conn.commit()
    conn.close()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return {"message": "Doctor deleted"}
