from pydantic import BaseModel
from pydantic.networks import int_domain_regex
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy import DateTime,Date, Float
from .database import Base

class Patientreg(BaseModel):
    regdate:str 
    name:str
    age:int
    fatherName:str
    marital:str
    sex    :str
    mobile :float
    address:str
    email:str  

class DoctorDiagnosis(BaseModel):
    umrno:int
    date :str
    admission : str
    diagnosis : str
    nextvisitdate : str
    docid : int

class DoctorRegistration(BaseModel):
    dept: str
    doctorfname: str
    doctorlname: str


class Visit(BaseModel):
    diagnosis: str
    clinicalsummary : str
    visitdate :str
    visitnumber : int
    umrno: int
    dept: str
    doctid: int

class OPdetails(BaseModel):
    medicine :str
    dose : str
    opdate : str
    investigations :str
    umrno:int
    unit:str
    doctid:int