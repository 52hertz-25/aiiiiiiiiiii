import sqlite3
from fastapi import FastAPI

app = FastAPI()

DB_PATH = "D:/data.db"

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


@app.get("/patients")
def get_patients():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, gender, age, phone FROM patient")
    rows = cur.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "gender": r[2], "age": r[3], "phone": r[4]} for r in rows]
from pydantic import BaseModel

# 定义输入模型
class PatientIn(BaseModel):
    name: str
    gender: str = "O"
    age: int = 0
    phone: str = ""

# 新增患者
@app.post("/patients")
def create_patient(p: PatientIn):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO patient (name, gender, age, phone) VALUES (?, ?, ?, ?)",
            (p.name, p.gender, p.age, p.phone),
        )
        pid = cur.lastrowid
    return {"id": pid, **p.dict()}

# 修改患者
@app.put("/patients/{pid}")
def update_patient(pid: int, p: PatientIn):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute(
            "UPDATE patient SET name=?, gender=?, age=?, phone=? WHERE id=?",
            (p.name, p.gender, p.age, p.phone, pid),
        )
        conn.commit()
    return {"id": pid, **p.dict()}

# 删除患者
@app.delete("/patients/{pid}")
def delete_patient(pid: int):
    with get_conn() as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM patient WHERE id=?", (pid,))
        conn.commit()
    return {"status": "deleted", "id": pid}
