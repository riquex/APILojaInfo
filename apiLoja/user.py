from .userManager import UserManager, validator
from os.path import join as path_join
from flask import Blueprint, request, json
from dotenv import dotenv_values

user = Blueprint('user', __name__)
config = dotenv_values(path_join('..', '.env'))

@user.route('/login', methods=['POST'])
def userLogin():
    form: json = request.get_json()


@user.route('/userinfo/<id>', methods=['GET'])
def getUserInfo(id):
    raise NotImplementedError("to be updated")

@user.route('/useraddress/<id>', methods=['GET'])
def getUserAddress(id):
    raise NotImplementedError("to be updated")