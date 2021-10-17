from typing import Text
from sqlalchemy import Column, Integer, String, ForeignKey,DateTime,Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql.operators import ColumnOperators, startswith_op
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Date
from .database import Base

class PatientRegistration(Base):
    __tablename__ = 'patient'
    umrno = Column(Integer,index=True, primary_key=True,autoincrement=True)
    regdate = Column(String)
    name =Column(String,nullable=False)
    age  = Column(Integer)
    fatherName = Column(String)
    marital = Column(String)
    sex     = Column(String)
    mobile  = Column(Float,nullable=False)
    address = Column(String)
    email = Column(String)

class DoctorDiagnosis(Base):
    __tablename__ ='doctordiag'
    id = Column(Integer,primary_key=True)
    umrno = Column(Integer,nullable=False)
    date = Column(String)
    admission = Column(String)
    diagnosis  = Column(String)
    nextvisitdate = Column(String)
    docid = Column(Integer)

class DoctorRegistration(Base):
    __tablename__ ='department'
    doctid = Column(Integer,primary_key=True,unique=True)
    dept = Column(String)
    doctorfname = Column(String)
    doctorlname = Column(String)

class Visit(Base):
    __tablename__ ='visits'
    id = Column(Integer,primary_key=True)
    dept = Column(String,ForeignKey('department.dept'))
    diagnosis = Column(String)
    clinicalsummary = Column(String)
    visitdate = Column(String)
    visitnumber =Column(Integer)
    umrno =Column(Integer,ForeignKey('patient.umrno'))
    doctid = Column(Integer)

class OPdetails(Base):
    __tablename__ ='opddetails'
    billno = Column(Integer,primary_key=True,autoincrement=True)
    medicine = Column(String)
    dose = Column(String)
    opdate = Column(String)
    investigations = Column(String)
    umrno =Column(Integer,ForeignKey('patient.umrno'))
    doctid = Column(Integer,ForeignKey('department.doctid'))
    unit = Column(String)

