from .produtosManager import ProdutosManager
from flask import render_template
from flask import make_response
from flask import Blueprint
from flask import Response
from flask import redirect

produtos = Blueprint('produtos', __name__)

@produtos.route('/produto/<id>', methods=['GET'])
def produto(id):
    
    return render_template('produto.html')