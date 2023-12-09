from .produtosManager import ProdutosManager
from flask import render_template
from flask import make_response
from flask import Blueprint
from flask import Response
from flask import redirect
from flask import request
from flask import abort

produtos = Blueprint('produtos', __name__)

@produtos.route('/get/product', methods=['GET', 'POST'])
def getProduct():
    if request.method == 'POST':
        if request.content_type.startswith('application/json'):
            form: dict = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()
        
        valido = all(key in form for key in ('idprod',))
        if valido:
            pass
    return abort(404)

@produtos.route('/get/product/image', methods=['GET', 'POST'])
def getProductImage():
    if request.method == 'POST':
        ...
    return abort(404)