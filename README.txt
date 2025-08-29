# 医疗管理系统 API (FastAPI + SQLite)

本项目是一个基于 **FastAPI** 和 SQLite 的简易医疗管理系统，提供病人、医生、预约、病历、处方、住院管理等接口。

---

## 📂 项目结构

api/
├── app/
│ ├── init.py
│ ├── main.py # 项目入口
│ ├── db.py # 数据库连接
│ ├── schemas.py # Pydantic 模型定义
│ └── routers/ # 路由模块
│ ├── patients.py
│ ├── doctors.py
│ ├── appointments.py
│ ├── case_records.py
│ ├── prescriptions.py
│ └── hospitalizations.py
├── data.db # SQLite 数据库
├── requirements.txt # 依赖
└── README.md # 项目说明

python -m venv .venv（创建虚拟环境）

激活虚拟环境
window
.venv\Scripts\activate（cmd）
.venv\Scripts\Activate.ps1（powershell）

linux
source .venv/bin/activate

pip install -r requirements.txt（安装依赖）

启动项目时在目录根运行uvicorn app.main:app --reload


📖 API 文档

启动成功后，浏览器访问：

Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

在这里可以直接测试 API。

🗄️ 数据库

默认使用 data.db（SQLite 数据库文件）

如果需要重建数据库，可以删除 data.db，重新运行项目后会自动创建（但表结构可能需要初始化 SQL 脚本）。

📌 已实现的功能
患者 (Patients)

GET /patients/ 列出所有患者

POST /patients/ 创建患者

PUT /patients/{pid} 更新患者信息

DELETE /patients/{pid} 删除患者

医生 (Doctors)

GET /doctors/ 列出所有医生

POST /doctors/ 创建医生

PUT /doctors/{id} 更新医生

DELETE /doctors/{id} 删除医生

预约 (Appointments)

GET /appointments/ 列出所有预约

POST /appointments/ 创建预约

PUT /appointments/{id} 更新预约

DELETE /appointments/{id} 删除预约

病历 (Case Records)

GET /case_records/ 列出所有病历

POST /case_records/ 创建病历

PUT /case_records/{id} 更新病历

DELETE /case_records/{id} 删除病历

处方 (Prescriptions)

GET /prescriptions/ 列出所有处方

POST /prescriptions/ 创建处方

PUT /prescriptions/{id} 更新处方

DELETE /prescriptions/{id} 删除处方

住院 (Hospitalizations)

GET /hospitalizations/ 列出所有住院记录

POST /hospitalizations/ 创建住院记录

PUT /hospitalizations/{id} 更新住院记录

DELETE /hospitalizations/{id} 删除住院记录
