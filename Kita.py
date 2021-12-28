from sqlalchemy import Column, text, REAL, Integer
from db_config import Base

class Kita(Base):
    __tablename__ = 'kita'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    floor = Column(Integer())
    num_of_student = Column(Integer())
    class_avg = Column(REAL())

    def __repr__(self):
        return f'\n<Kita id={self.id} floor ={self.floor} number of students = {self.num_of_student}, class avg={self.class_avg} >'

    def __str__(self):
        return f'\n<Kita id={self.id} floor ={self.floor} number of students = {self.num_of_student}, class avg={self.class_avg} >'
