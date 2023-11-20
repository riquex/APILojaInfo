from .lojaManager import LojaManager
from .userManager import UserManager
from flask import render_template
from flask import make_response
from flask import Blueprint
from flask import request
from flask import g

loja = Blueprint('loja', __name__)

@loja.route('/', methods=['GET'])
def index():
    context = {}
    if g.username:
        context['username'] = g.username
    response = make_response(render_template('index_test.html', **context))
    return response