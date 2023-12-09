from .adminManager import AdminManager
from .userManager import UserManager
from flask import render_template
from flask import make_response
from traceback import print_exc
from flask import Blueprint
from flask import Response
from flask import jsonify
from flask import request
from io import BytesIO
from PIL import Image
from flask import g
import base64
import re

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def indexAdmin():
    return render_template('admin.html')

@admin.route('/admin/cadastroproduto')
def cadastroProduto():
    return render_template('cadastrarproduto.html')

@admin.route('/admin/fetchusersall', methods=['GET', 'POST'])
def fetchUsersAll():
    argumentos_pesquisa = dict()
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            form: dict[str | list, str|int|list] = request.get_json()

            if isinstance(form, dict):
                chaves_validas = [key for key in form if key in ('column', 'stringlike', 'start')]
                for key in chaves_validas:
                    argumentos_pesquisa[key] = form[key]

    return jsonify(
            [user.comoDicionario() for user in UserManager().pegarTodosUsuarios(**argumentos_pesquisa)]
        )

@admin.route('/admin/gerenciarusuarios')
def gerenciarUsuarios():
    context = dict()
    return render_template('gerenciarusuarios.html', **context)

@admin.route('/admin/test')
def test():
    return render_template('layout/neo_admin.html')

@admin.route('/admin/test/cadastroproduto', methods=['GET', 'POST'])
def testCadastropoduto():
    response = make_response(render_template('neo_cadastroproduto.html'))
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            form: dict[str | list, str|int|list] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = all(key in form for key in ('nome', 'preco', 'image-text', 'image64', 'descricao'))
        if valido:
            try:
                image64 = form['image64']
                hearder, image64 = image64.split(',')
                form['image64'] = hearder
                imagebytes = base64.b64decode(image64, validate=True)
                img = Image.open(BytesIO(imagebytes)).convert('RGB')

                price = re.sub(pattern=r'\D', repl='', string=form['preco'])

                code = AdminManager().InsercaoCompletaProduto(
                    form['nome'][:128],
                    form['descricao'][:512],
                    price,
                    9999999,
                    img
                )

                response = Response(status=200) if code == 1 else Response(500)
                print('product registration: ', code)
            except:
                print_exc()
                response = Response(status=500)
        else:
            response = Response(status=400)
    return response
@admin.route('/admin/test/gerenciarusuarios')
def testGerenciarUsuarios():
    return render_template('neo_gerenciarusuarios.html')

@admin.route('/admin/test/gerenciarprodutos')
def testGerenciarProdutos():
    return render_template('neo_gerenciarprodutos.html')