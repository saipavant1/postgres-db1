from fastapi import FastAPI, Depends, status, Response, HTTPException
from pydantic.networks import HttpUrl
from starlette import responses
from . import schemas, models
from .database import SessionLocal, engine
import uvicorn
from sqlalchemy.orm import Session,relationship
from typing import List
from passlib.context import CryptContext
app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def homepage():
    return "Hello world"

@app.post("/patientreg",tags=['patientreg'])
def create(request: schemas.Patientreg,db: Session = Depends(get_db)):
    #new_reg = models.PatientRegistration(umrno=request.umrno,name=request.name,age=request.age,email=request.email)
    new_reg = models.PatientRegistration(regdate =request.regdate, 
                                        name =request.name, 
                                        age  =request.age, 
                                        fatherName = request.fatherName, 
                                        marital = request.marital,
                                        sex     = request.sex,
                                        mobile  = request.mobile,
                                        address =request.address,
                                        email =request.email)
    db.add(new_reg)
    db.commit()
    db.refresh(new_reg)
    return new_reg






@app.get("/patientreg/{umrno}",tags=['patientreg'])
def get_user(umrno, db: Session= Depends(get_db)):
    user = db.query(models.PatientRegistration).filter(models.PatientRegistration.umrno == umrno).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with {umrno} doesnot exist ") 
    return user

@app.post("/doctorregistation",tags=['doctor'])
def doctorid_create(request: schemas.DoctorRegistration,db: Session = Depends(get_db)):
    doctreg = models.DoctorRegistration(dept=request.dept,doctorfname=request.doctorfname,doctorlname=request.doctorlname)
    db.add(doctreg) 
    db.commit()
    db.refresh(doctreg)
    return doctreg

@app.post("/doctordiagnosis",tags=['doctor'])
def doctorid_create(request: schemas.DoctorDiagnosis,db: Session = Depends(get_db)):
    doctdiag = models.DoctorDiagnosis(date=request.date,admission=request.admission, 
                                    diagnosis=request.diagnosis,nextvisitdate=request.nextvisitdate,
                                    docid=request.docid,umrno=request.umrno)
    db.add(doctdiag) 
    db.commit()
    db.refresh(doctdiag)
    return doctdiag



@app.post("/visit",tags=['visits'])
def visit_create(request: schemas.Visit,db: Session = Depends(get_db)):
    patient_visit = models.Visit(diagnosis = request.diagnosis, 
                                clinicalsummary = request.clinicalsummary,
                                visitdate = request.visitdate, 
                                visitnumber = request.visitnumber,umrno=request.umrno,
                                dept = request.dept, doctid = request.doctid, )
    db.add(patient_visit) 
    db.commit()
    db.refresh(patient_visit)
    return patient_visit

@app.post("/opdetails",tags=['opdetails'])
def opdetails(request: schemas.OPdetails, db: Session =Depends(get_db)):
    opdetails = models.OPdetails(medicine =request.medicine,
                                dose = request.dose, opdate=request.opdate, 
                                investigations = request.investigations,
                                unit=request.unit,doctid=request.doctid,umrno=request.umrno)
    db.add(opdetails) 
    db.commit()
    db.refresh(opdetails)
    return opdetails

@app.get("/opdetails/{umrno}",tags=['opreg'])
def get_user(umrno, db: Session= Depends(get_db)):
    user = db.query(models.OPdetails).filter(models.OPdetails.umrno == umrno).all()
    if not user:
        raise HTTPException(status_code=404, detail=f"No record for the patient with UMR {umrno} ")
    return user

