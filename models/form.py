from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase
from database import db



class Form(BaseModel):
    Name = pw.CharField()
    UserID = pw.CharField(default = "")
    Gender = pw.CharField(unique=False)
    Birthdate = pw.DateTimeField()
    Address = pw.CharField()
    Medications = pw.CharField()
    Nameofnextkin = pw.CharField()
    Phoneofnextkin = pw.CharField()
    Reasonforvisit = pw.CharField()
    Fever = pw.CharField()
    Headache = pw.CharField()
    Nightchills = pw.CharField()
    Sorethroat = pw.CharField()
    Cough = pw.CharField()
    Breathingdiff = pw.CharField()
    Diarrhoea = pw.CharField()
    Chestpain = pw.CharField()
    Legnumbness = pw.CharField()
    Handnumbness = pw.CharField()
    Abdominalpain = pw.CharField(default="False")
    Vomit = pw.CharField()
    Dizziness = pw.CharField()
    Sleepingdiff = pw.CharField()
    Facenumbness = pw.CharField()
    Diabetes = pw.CharField()
    Highbloodpressure = pw.CharField()
    Highcholesterol = pw.CharField()
    Asthma = pw.CharField()
    Kidneydisease = pw.CharField()
    Arthritis = pw.CharField()
    Cancer = pw.CharField()
    Liverdisease = pw.CharField()
    Stroke = pw.CharField()
    COPD = pw.CharField()
    Depression = pw.CharField()
    Alzheimer = pw.CharField()
