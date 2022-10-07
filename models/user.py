from models.base_model import BaseModel
import peewee as pw
from playhouse.postgres_ext import PostgresqlExtDatabase
from database import db

class User(BaseModel):
    Username = pw.CharField(unique=False)
    Password = None
    Password_hash = pw.CharField()
