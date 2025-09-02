# routers/student_router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import SessionLocal
import models, schemas

router = APIRouter(prefix="/students", tags=["Students"])

# Dependency get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET semua siswa
@router.get("/", response_model=list[schemas.Student])
def get_students(db: Session = Depends(get_db)):
    return db.query(models.Student).all()

# GET siswa by ID
@router.get("/{id_siswa}", response_model=schemas.Student)
def get_student(id_siswa: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id_siswa == id_siswa).first()
    if not student:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    return student

# POST tambah siswa
@router.post("/", response_model=dict, status_code=status.HTTP_201_CREATED)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    try:
        new_student = models.Student(name=student.name, balance_saldo=student.balance_saldo)
        db.add(new_student)
        db.commit()
        db.refresh(new_student)

        return {
            "status": "success",
            "message": f"Siswa '{new_student.name}' berhasil ditambahkan",
            "student": {
                "id_siswa": new_student.id_siswa,
                "name": new_student.name,
                "balance_saldo": new_student.balance_saldo
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={
            "status": "error",
            "message": f"Gagal menambahkan siswa: {str(e)}"
        })

# PUT update siswa (nama & saldo)
@router.put("/{id_siswa}", response_model=dict)
def update_student(id_siswa: int, data: schemas.StudentUpdate, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id_siswa == id_siswa).first()
    if not student:
        raise HTTPException(status_code=404, detail={"status": "error", "message": "Siswa tidak ditemukan"})

    try:
        updated_fields = []
        if data.name is not None:
            student.name = data.name
            updated_fields.append("name")
        if data.balance_saldo is not None:
            student.balance_saldo = data.balance_saldo
            updated_fields.append("balance_saldo")

        if not updated_fields:
            return {"status": "warning", "message": "Tidak ada data yang diubah"}

        db.commit()
        db.refresh(student)

        return {
            "status": "success",
            "message": f"Siswa dengan id {id_siswa} berhasil diperbarui",
            "updated_fields": updated_fields,
            "student": {
                "id_siswa": student.id_siswa,
                "name": student.name,
                "balance_saldo": student.balance_saldo
            }
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail={"status": "error", "message": f"Gagal memperbarui siswa: {str(e)}"})


# DELETE siswa
@router.delete("/{id_siswa}", status_code=status.HTTP_200_OK)
def delete_student(id_siswa: int, db: Session = Depends(get_db)):
    student = db.query(models.Student).filter(models.Student.id_siswa == id_siswa).first()
    if not student:
        raise HTTPException(status_code=404, detail="Siswa tidak ditemukan")
    db.delete(student)
    db.commit()
    return {"message": f"Siswa dengan id {id_siswa} berhasil dihapus"}
