from flask import Blueprint
from app import app
from flask_cors import CORS
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt
import peewee as pw
import datetime
from database import db


records_api_blueprint = Blueprint('records_api',
                             __name__,
                             template_folder='templates')

@records_api_blueprint.route('/', methods=['GET'])
def index():
    all_records = Form.select()
    all_records = [model_to_dict(record) for record in all_records]

    return jsonify(all_records)

@records_api_blueprint.route("/create", methods = ["POST"])
def create():
    
    print("connected")
    new_entry = request.get_json()
    print('new_entry')
    print(new_entry)

    current_time = datetime.datetime.now
    now = print(current_time)

    print(new_entry['Asthma'])
    print(new_entry['Livercancer'])

    create = Form.create(Name = new_entry['Name'], UserID = new_entry['ID'], Gender = new_entry['Gender'], Birthdate = new_entry['Birthdate'], 
    Address = new_entry['Address'], Medications = new_entry['Medications'], Nameofnextkin = new_entry['Nameofnextkin'],
    Phoneofnextkin = new_entry['Phoneofnextkin'], Reasonforvisit = new_entry['Reasonforvisit'], Fever = new_entry['Fever'], 
    Headache = new_entry['Headache'], Nightchills = new_entry['Nightchills'], Sorethroat = new_entry['Sorethroat'], Cough = new_entry['Cough'], 
    Breathingdiff = new_entry['Breathingdiff'], Diarrhoea = new_entry['Diarrhoea'], Chestpain = new_entry['Chestpain'], 
    Legnumbness = new_entry['Legnumbness'], Handnumbness = new_entry['Handnumbness'], Facenumbness = new_entry['Facenumbness'], 
    Abdominalpain =  new_entry['Abdominalpain'], Diabetes = new_entry['Diabetes'], Highbloodpressure = new_entry['Highbloodpressure'], 
    Highcholesterol = new_entry['Highcholesterol'], Asthma = new_entry['Asthma'], Kidneydisease = new_entry['Kidneydisease'],
    Arthritis = new_entry['Arthritis'], Pancreaticcancer = new_entry['Pancreaticcancer'], Livercancer = new_entry['Livercancer'], 
    Colorectalcancer = new_entry['Colorectalcancer'], COPD = new_entry['COPD'], Depression = new_entry['Depression'], 
    Lungcancer = new_entry['Lungcancer'])


    message = []
    message.append(create.id)
    
    return jsonify({'message' : message})

@records_api_blueprint.route("/update")
def update():
    return

@records_api_blueprint.route("/delete")
def delete():

    return 


@records_api_blueprint.route("/show", methods = ["POST"])
def show():
    
    print("connected")
    user_input = request.get_json()
    print('user_input')
    print(user_input)

    record_exists = Form.get_or_none(Form.id == user_input['id'], Form.Name == user_input['Name'])
    
    record_details = []
    
    if record_exists:
        record_details.append([{'id':record_exists.id, 'Name': record_exists.Name, 'Createdon': record_exists.created_at, 
        'Gender': record_exists.Gender, 'Birthdate': record_exists.Birthdate, 
        'Address': record_exists.Address, 'Medications': record_exists.Medications, 
        'Nameofnextkin': record_exists.Nameofnextkin, 'Phoneofnextkin': record_exists.Phoneofnextkin,
        'Reasonforvisit': record_exists.Reasonforvisit, 'Errormessage': "",
        'Fever': record_exists.Fever, 'Headache': record_exists.Headache, 'Nighchills': record_exists.Nightchills,
        'Sorethroat': record_exists.Sorethroat, 'Cough': record_exists.Cough, 'Breathingdiff': record_exists.Breathingdiff,
        'Diarrhoea': record_exists.Diarrhoea, 'Chestpain': record_exists.Chestpain, 'Legnumbness': record_exists.Legnumbness,
        'Handnumbness': record_exists.Handnumbness, 'Facenumbness': record_exists.Facenumbness, 
        'Abdominalpain': record_exists.Abdominalpain, 'Diabetes': record_exists.Diabetes,
        'Highbloodpressure': record_exists.Highbloodpressure, 'Highcholesterol': record_exists.Highcholesterol, 
        'Asthma': record_exists.Asthma, 'Kidneydisease': record_exists.Kidneydisease, 'Arthritis': record_exists.Arthritis,
        'Pancreaticcancer': record_exists.Pancreaticcancer, 'Livercancer': record_exists.Livercancer, 
        'Colorectalcancer': record_exists.Colorectalcancer, 'COPD': record_exists.COPD, 'Depression': record_exists.Depression, 
        'Lungcancer': record_exists.Lungcancer
         }])

    
    else: 
        record_details.append([{'id':"", 'Name': "", 'Createdon': "", 
        'Gender': "", 'Birthdate': "", 
        'Address': "", 'Medications': "", 
        'Nameofnextkin': "", 'Phoneofnextkin': "",
        'Reasonforvisit': "", 'Errormessage': "Record does not exist.", 
        'Fever': "", 'Headache': "", 'Nighchills': "",
        'Sorethroat': "", 'Cough': "", 'Breathingdiff': "",
        'Diarrhoea': "", 'Chestpain': "", 'Legnumbness': "",
        'Handnumbness': "", 'Facenumbness': "", 
        'Abdominalpain': "", 'Diabetes': "",
        'Highbloodpressure': "", 'Highcholesterol': "", 
        'Asthma': "", 'Kidneydisease': "", 'Arthritis': "",
        'Pancreaticcancer': "", 'Livercancer': "", 
        'Colorectalcancer': "", 'COPD': "", 'Depression': "", 'Lungcancer': ""}])

    print(record_details)

    return jsonify({'record_details' : record_details})
