# 🚀 Task Manager API (FastAPI + PostgreSQL + JWT)

A simple backend project built using **FastAPI** that allows users to manage tasks with full CRUD operations and secure APIs using JWT authentication.

---

## 📌 Features

- ✅ FastAPI backend
- ✅ PostgreSQL database connection
- ✅ Create, Read, Update, Delete (CRUD) APIs
- ✅ Input validation using Pydantic
- ✅ Error handling with HTTPException
- ✅ JWT Authentication (Login + Secure APIs)
- ✅ Swagger UI for API testing

---

## 📁 Project Structure


task_manager/
├── main.py
├── database.py
├── models.py
├── schemas.py
├── auth.py


---

## ⚙️ Installation

### 1️⃣ Clone Repository


git clone https://github.com/payal-morepatil/task-manager-api.git

cd task-manager-api


---

### 2️⃣ Create Virtual Environment


python -m venv venv
.\venv\Scripts\activate


---

### 3️⃣ Install Dependencies


pip install fastapi uvicorn sqlalchemy psycopg2-binary python-jose


---

## 🗄️ Database Setup (PostgreSQL)

### Create Database

```sql
CREATE DATABASE taskdb;
▶️ Run Project
uvicorn main:app --reload
🌐 API Documentation

Swagger UI:

http://127.0.0.1:8000/docs
🔐 Authentication (JWT)
Login API
POST /login

Input:

username = admin
password = admin
Use Token
Copy token from login response
Click Authorize in Swagger
Paste:
Bearer your_token_here
📌 API Endpoints
Method	Endpoint	Description
POST	/login	Generate token
POST	/tasks	Create task
GET	/tasks	Get all tasks
GET	/tasks/{id}	Get task by ID
PUT	/tasks/{id}	Update task
DELETE	/tasks/{id}	Delete task
🧪 Example Request
{
  "title": "Study",
  "description": "Learn FastAPI",
  "status": "pending"
}
🎯 Learning Outcomes
Understanding REST APIs
Working with FastAPI
Database integration with PostgreSQL
JWT Authentication
Error handling
