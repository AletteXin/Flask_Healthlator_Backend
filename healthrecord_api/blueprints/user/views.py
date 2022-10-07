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


# @users_api_blueprint.route('/show', methods=["GET"])
# @login_required
# def show(show_username):
    
#     if session.get('user_id'):
#         user = User.get_or_none(User.id == session["user_id"])
#     else:
#         user = None 
    
#     show_user = User.get_or_none(User.username == show_username)

#     if show_user:
#         show_username = show_user.username
#         images = Image.select().where(Image.user_id == show_user.id).order_by(Image.date_posted.desc())
#         approval_record = Follow.get_or_none(Follow.follower == user, Follow.idol == show_user)
#         show_idols = User.select().join(Follow, on = Follow.idol_id == User.id).where(Follow.follower_id == show_user.id, Follow.approved == "1")
#         length_si = show_idols.count()
#         user_liked = Image.select().join(Likes, on = Likes.liker_id == user.id).where(Likes.image_id == Image.id)


#         return render_template('/users/profile.html', show_user = show_user, approval_record = approval_record, images = images, 
#         show_idols = show_idols,  length_si = length_si, user_liked = user_liked)

        
#     else:
#         return redirect (url_for('login.new'))



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

    