from fastapi import FastAPI
from database import engine, SessionLocal, Base
import models
from routers import student_router

app = FastAPI(title="Students API")

# Auto create tables
Base.metadata.create_all(bind=engine)

# Seeder default data
def seed_data():
    db = SessionLocal()
    if db.query(models.Student).count() == 0:  # kalau tabel kosong
        default_students = [
            models.Student(name="Ayu", balance_saldo=15000),
            models.Student(name="Budi", balance_saldo=22000),
        ]
        db.add_all(default_students)
        db.commit()
    db.close()

seed_data()

# Register Router
app.include_router(student_router.router)
