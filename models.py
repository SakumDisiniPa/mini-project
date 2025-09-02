from sqlalchemy import Column, Integer, String
from database import Base

class Student(Base):
    __tablename__ = "students"

    id_siswa = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    balance_saldo = Column(Integer, default=0)
