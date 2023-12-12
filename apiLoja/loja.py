from .produtosManager import ProdutosManager
from .lojaManager import LojaManager
from .userManager import UserManager
from flask import render_template
from flask import make_response
from flask import Blueprint
from flask import redirect
from flask import Response
from flask import request
from pathlib import Path
from flask import abort
from flask import g
import re

loja = Blueprint('loja', __name__)

@loja.route('/', methods=['GET'])
def index():
    context = {}
    if g.username:
        context['username'] = g.username
    context['products'] = LojaManager().listaAleatoriaDeProdutos()
    response = make_response(render_template('index.html', **context))
    return response

@loja.route('/produto/<id>', methods=['GET'])
def produto(id):
    context = {}
    prod = ProdutosManager().pegarProduto(id)
    if prod == -1: abort(404)
    if g.username: context['username'] = g.username
    context['produto'] = prod.comoLista()
    context['produto'][3] = prod.valorEstilizado()
    staticlink = Path(context['produto'][5]).as_posix()
    context['produto'][5] = re.sub(pattern=r'\/?static\/', repl='',string=staticlink)
    response = make_response(render_template('produtopagina.html', **context))
    return response

@loja.route('/carrinho', methods=['GET', 'POST', 'PUT', 'DELETE'])
def carrinho():
    if g.userid is None: return redirect('/login')

    if request.method in ('POST', 'PUT', 'DELETE'):
        response = Response(status='201')
        if request.content_type.startswith('application/json'):
            form: dict | list[dict] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = all(key in form for key in ('idProduto', 'quantidade'))
        pode_apagar = 'idProduto' in form

        if valido:
            code = LojaManager().adicionarAoCarrinho(idCliente=g.userid, **form)
            if code == 0:
                response.status = '500'
        elif request.method == 'DELETE' and pode_apagar:
            code = LojaManager().removerItemdoCarrinho(idCliente=g.userid, **form)
            if code == 0:
                response.status = '500'
        else: response.status = '400'
    else:
        context = {'username': g.username}
        result = LojaManager().pegarCarrinhoDoCliente(g.userid)
        if result != -1:
            context['prods'] = [ProdutosManager().pegarProduto(row[1]).comoListaEstilizadoNotStatic() + list(row) for row in result]
        response = make_response(render_template('carrinho_test.html', **context))
    return response 