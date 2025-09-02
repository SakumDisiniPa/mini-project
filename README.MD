# 🎓 Student App (FastAPI)

A simple **CRUD REST API** built with FastAPI, SQLAlchemy, and Pydantic for managing student data.  

---

## 📂 Project Structure
```

student\_app/
│── main.py              # Entry point FastAPI
│── models.py            # SQLAlchemy models
│── schemas.py           # Pydantic schemas
│── database.py          # Database config
│── routers/
│   └── student\_router.py # CRUD routes
│── requirements.txt     # Dependencies
│── README.md            # Project documentation

````

---

## 🛠️ Requirements
- Python 3.10+
- pip

### Install dependencies
```bash
pip install -r requirements.txt
````

---

## ▶️ Running the App

1. Start FastAPI server:

```bash
uvicorn main:app --reload
```

2. Open in browser:

```
http://127.0.0.1:8000/docs
```

---

## 📡 API Endpoints

### Get all students

```http
GET /students/
```

### Get student by ID

```http
GET /students/{id}
```

### Add student

```http
POST /students/
Content-Type: application/json

{
  "name": "Budi",
  "balance_saldo": 10000
}
```

### Update student

```http
PUT /students/{id}
Content-Type: application/json

{
  "name": "Andi",
  "balance_saldo": 20000
}
```

### Delete student

```http
DELETE /students/{id}
```

---

## 🧪 Testing

You can test the endpoints using:

* **Postman**
* **curl**
* **Browser** (for GET endpoints)

### Example with curl

```bash
# Get all students
curl -X GET http://127.0.0.1:8000/students/

# Add a new student
curl -X POST http://127.0.0.1:8000/students/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Dodo Sidodo", "balance_saldo": 10000}'
  
#Update
curl -X PUT http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Siti",
    "balance_saldo": 25000
  }'
```

### 👉 Keterangan:

* `PUT` → method untuk update
* `http://127.0.0.1:8000/students/1` → `1` adalah **id\_siswa** yang mau diubah
* `-H "Content-Type: application/json"` → header supaya server tahu kita kirim JSON
* `-d` → data body JSON

Kalau misalnya mau update **hanya salah satu field** (misal cuma `balance_saldo`), bisa gini:

```bash
curl -X PUT http://127.0.0.1:8000/students/1 \
  -H "Content-Type: application/json" \
  -d '{
    "balance_saldo": 50000
  }'
```
