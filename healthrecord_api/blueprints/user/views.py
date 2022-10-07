from flask import Blueprint
from app import app
from flask_cors import CORS
from models.user import User
from models.form import Form
from flask import Blueprint, jsonify, request
from playhouse.shortcuts import model_to_dict, dict_to_model
import json
import datetime as dt
import peewee as pw
import datetime
from database import db
from werkzeug.security import generate_password_hash, check_password_hash


users_api_blueprint = Blueprint('users_api',
                            __name__,
                            template_folder='templates')


@users_api_blueprint.route('/create', methods=['POST'])
def create():

    print("connected")
    new_entry = request.get_json()
    print('new_entry')
    print(new_entry)

    new_username = new_entry['Username']
    new_password = new_entry['Password']
    new_repassword = new_entry['RePassword']

    if new_password != new_repassword:
        message = ["Passwords do not match. Please reenter details."]
        return jsonify({'message' : message})
    
    create = User.create(Username = new_username, Password_hash = generate_password_hash(new_password))
    message = ["Account created."]
    return jsonify({'message' : message})


@users_api_blueprint.route('/show', methods=["POST"])
def show():
    
    print("connected")
    user_input = request.get_json()
    print('user_input')
    print(user_input)

    new_username = user_input['Username']
    new_password = user_input['Password']

    login_details = []

    user = User.get_or_none(User.Username == new_username)
    if user and check_password_hash(user.Password_hash, new_password):
        login_details.append([{'id': user.id, 'Username': user.Username, 'Errormessage': ""}])

    else: 
        login_details.append([{'id': "", 'Username': "", 'Errormessage': "Invalid login details. Please try again."}])

    return jsonify({'login_details' : login_details})

@users_api_blueprint.route('/showrecords', methods=["POST"])
def showrecords():

    print("connected")
    user_input = request.get_json()
    print('user_input')
    print(user_input)

    token = user_input['token']

    login_details = []

    forms = Form.get_or_none(Form.UserID == token)
    
    records = []
    
    if len(forms) > 0:

        for form in forms:
            records.append([{'id':form.id, 'Name': form.Name, 
            'Gender': form.Gender, 'Birthdate': form.Birthdate, 
            'Address': form.Address, 'Medications': form.Medications, 
            'Nameofnextkin': form.Nameofnextkin, 'Phoneofnextkin': form.Phoneofnextkin,
            'Reasonforvisit': form.Reasonforvisit, 'Errormessage': "",
            'Fever': form.Fever, 'Headache': form.Headache, 'Nighchills': form.Nightchills,
            'Sorethroat': form.Sorethroat, 'Cough': form.Cough, 'Breathingdiff': form.Breathingdiff,
            'Diarrhoea': form.Diarrhoea, 'Chestpain': form.Chestpain, 'Legnumbness': form.Legnumbness,
            'Handnumbness': form.Handnumbness, 'Facenumbness': form.Facenumbness, 
            'Abdominalpain': form.Abdominalpain, 'Diabetes': form.Diabetes,
            'Highbloodpressure': form.Highbloodpressure, 'Highcholesterol': form.Highcholesterol, 
            'Asthma': form.Asthma, 'Kidneydisease': form.Kidneydisease, 'Arthritis': form.Arthritis,
            'Pancreaticcancer': form.Pancreaticcancer, 'Livercancer': form.Livercancer, 
            'Colorectalcancer': form.Colorectalcancer, 'COPD': form.COPD, 'Depression': form.Depression, 
            'Lungcancer': form.Lungcancer
            }])
        

    else: 
        records.append([{'id':"", 'Name': "", 
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


    return jsonify({'records' : records})


# @users_api_blueprint.route('/update/<field>', methods=['POST'])
# @login_required
# def update(field):
#     # if session.get('user_id'):
#     #     user = User.get_or_none(User.id == session['user_id'])
#     if current_user:
#         new_info = request.form[field]
            
#         if field == "email":
#             email_existing = User.get_or_none(User.email == new_info)
#             if email_existing:
#                 flash("There is an existing account associated with this email.")
#                 return redirect (url_for('users.edit'))
            
#         if field == "username":
#             existing_username = User.get_or_none(User.username == new_info)
#             if existing_username:
#                 flash("Sadly, this username has been taken. Please choose another.")
#                 return redirect (url_for('users.edit'))
            
#         if field == "password":
#             reenter_password = request.form['reenter_password']

#             if new_info != reenter_password:
#                 flash("Passwords do not match. Please reenter details.")
#                 return redirect (url_for('users.edit'))

#         if field == "privacy":
#             if new_info == "Public":
#                 new_info = "1"
#             else:
#                 new_info = "0"

#         setattr(current_user, field, new_info)
#         current_user.save()

#         flash("Your info has been updated.")
#     else:
#         flash("An error occured, please try again.")
#     return redirect (url_for('users.edit'))

#     # else:
#     #     flash("An error occured, please try again.")
#     #     return redirect (url_for('users.edit'))

    