import sqlite3
import os

# 确认数据库路径：放在项目根目录下的 data.db
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "..", "data.db")

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    # 1) 患者表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS patient (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        gender TEXT,
        age INTEGER,
        phone TEXT,
        id_number TEXT,
        address TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 2) 医生表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS doctor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT,
        title TEXT,
        phone TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    # 3) 预约表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS appointment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        appt_time TEXT NOT NULL,
        status TEXT,
        note TEXT,
        FOREIGN KEY(patient_id) REFERENCES patient(id) ON DELETE CASCADE,
        FOREIGN KEY(doctor_id) REFERENCES doctor(id) ON DELETE CASCADE
    )
    """)

    # 4) 病历表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS case_record (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        doctor_id INTEGER NOT NULL,
        visit_time TEXT NOT NULL,
        diagnosis TEXT,
        symptoms TEXT,
        treatment TEXT,
        FOREIGN KEY(patient_id) REFERENCES patient(id),
        FOREIGN KEY(doctor_id) REFERENCES doctor(id)
    )
    """)

    # 5) 处方表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS prescription (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        case_id INTEGER NOT NULL,
        drug_name TEXT,
        dosage TEXT,
        frequency TEXT,
        duration TEXT,
        FOREIGN KEY(case_id) REFERENCES case_record(id)
    )
    """)

    # 6) 住院表
    cur.execute("""
    CREATE TABLE IF NOT EXISTS hospitalization (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_id INTEGER NOT NULL,
        doctor_id INTEGER,
        admit_time TEXT NOT NULL,
        discharge_time TEXT,
        ward TEXT,
        bed_no TEXT,
        status TEXT DEFAULT 'admitted',
        FOREIGN KEY(patient_id) REFERENCES patient(id),
        FOREIGN KEY(doctor_id) REFERENCES doctor(id)
    )
    """)

    conn.commit()
    conn.close()
    print("✅ 数据库初始化完成！")
