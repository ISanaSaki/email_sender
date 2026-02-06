# 📧 Email Sender (Fake)

A mini backend project built with **FastAPI** that simulates sending emails using **async background jobs**, **rate limiting**, and a **task queue** architecture.

This project is designed for learning and practicing real-world backend concepts such as API design, async processing, Celery, Redis, PostgreSQL, and database migrations.

> ⚠️ Email sending is **fake** and implemented only for educational purposes.

---

## 🚀 Features

- REST API built with **FastAPI**
- Single endpoint to submit email sending requests
- **Rate limiting** (e.g. max 3 requests per minute per IP)
- Request persistence using **PostgreSQL**
- Database migrations with **Alembic**
- Asynchronous task processing using **Celery**
- **Redis** as message broker / backend
- Clean project structure (API, services, tasks, schemas)

---

## 📌 API Endpoint

### `POST /send-email`

Submit a fake email sending request.

#### Request Body

```json
{
  "email": "user@example.com",
  "message": "Hello from FastAPI"
}
```

---

##  Workflow

1.Request is rate-limited based on client IP.

2.Request data is stored in PostgreSQL.

3.A Celery background task is triggered.

4.The task simulates sending an email asynchronously.

---

## 🗂 Project Structure
```
├── alembic
│   ├── versions
│   │   └── create_email_requests_table.py
│   ├── env.py
│   └── script.py.mako
│
├── app
│   ├── api
│   │   ├── deps.py
│   │   └── routes.py
│   ├── core
│   │   ├── celery_app.py
│   │   ├── config.py
│   │   └── redis.py
│   ├── db
│   │   ├── base.py
│   │   ├── models.py
│   │   └── session.py
│   ├── schemas
│   │   └── email.py
│   ├── services
│   │   └── email_service.py
│   ├── tasks
│   │   ├── email.py
│   │   └── email_tasks.py
│   └── main.py
│
├── .env
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

---

### 🧪 Tech Stack

-Python

-FastAPI

-PostgreSQL

-SQLAlchemy

-Alembic

-Celery

-Redis

-Uvicorn

---

### ⚙️ Environment Variables

Create a .env file in the root directory of the project:
```
DATABASE_URL=postgresql+psycopg2://postgres:PASSWORD@localhost:5432/email_sender
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
POSTGRES_PASSWORD=PASSWORD
```

---

## ⚙️ Setup & Run 

1️⃣ Create virtual environment & install dependencies
```bash
python -m venv venv
venv\Scripts\activate 
pip install -r requirements.txt
```
2️⃣ Run database migrations

Make sure PostgreSQL is running and the database exists.
```bash
alembic upgrade head
```
3️⃣ Start FastAPI application
```bash
uvicorn app.main:app --reload
```

Application will be available at:

-http://127.0.0.1:8000


Swagger UI:

-http://127.0.0.1:8000/docs

4️⃣ Start Redis

Make sure Redis server is running locally:
```bash
redis-server
```
5️⃣ Run Celery worker
```bash
celery -A app.core.celery_app worker --loglevel=info
```
