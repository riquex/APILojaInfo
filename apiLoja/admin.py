from flask import render_template
from .userManager import UserManager
from flask import Blueprint
from flask import jsonify
from flask import request
from io import BytesIO
from PIL import Image
from flask import g
import base64

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
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            form: dict[str | list, str|int|list] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()
        
        valido = all(key in form for key in ('nome', 'preco', 'image-text', 'image64', 'descricao'))
        if valido:
            image64 = form['image64']
            imagebytes = base64.b64decode(image64, validate=True)
            img = Image.open(BytesIO(imagebytes))
            img.save('gg.png')

        print(form.keys(),)
    return render_template('neo_cadastroproduto.html')

@admin.route('/admin/test/gerenciarusuarios')
def testGerenciarUsuarios():
    return render_template('neo_gerenciarusuarios.html')

@admin.route('/admin/test/gerenciarprodutos')
def testGerenciarProdutos():
    return render_template('neo_gerenciarprodutos.html')