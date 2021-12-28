from sqlalchemy import Column, BigInteger,Integer, String, DateTime, REAL, Date, ForeignKey, UniqueConstraint
from db_config import Base
from sqlalchemy.orm import relationship, backref
from Kita import Kita

class Students(Base):
    __tablename__ = 'student'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    fname = Column(String(50), nullable=False)
    lname = Column(String(50), nullable=False)
    grade_avg = Column(Integer(), nullable=False)
    kita_id = Column(Integer(), ForeignKey('kita.id'), nullable=False)

    kitot = relationship('Kita', backref=backref('student', uselist=True))

    __table_args__ = (UniqueConstraint('fname', 'lname', name='una_1'),)

    def __repr__(self):
        return f'\n<Student id={self.id} first name={self.fname} last name={self.lname}, grade avg={self.grade_avg},kita id={self.kita_id} >'

    def __str__(self):
        return f'\n<Student id={self.id} first name={self.fname} last name={self.lname}, grade avg={self.grade_avg},kita id={self.kita_id} >'
