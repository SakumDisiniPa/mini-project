# schemas.py
from pydantic import BaseModel

class StudentBase(BaseModel):
    name: str
    balance_saldo: int

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    name: str | None = None 
    balance_saldo: int | None = None

class Student(StudentBase):
    id_siswa: int

    class Config:
        from_attributes = True

