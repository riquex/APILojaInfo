from flask import render_template
from .userManager import UserManager
from flask import Blueprint
from flask import jsonify
from flask import request
from flask import g

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def indexAdmin():
    return render_template('admin.html')

@admin.route('/admin/cadastroproduto')
def cadastroProduto():
    return render_template('cadastrarproduto.html')

@admin.route('/admin/fetchusersall', methods=['GET', 'POST'])
def fetchUsersAll():
    if request.method == "POST":
        if request.content_type.startswith('application/json'):
            form: dict = request.get_json()

            valido = all(key in form for key in ('column', 'stringlike'))
            print(form)
            if valido:
                return jsonify(
                    [user.comoDicionario() for user in UserManager().pegarTodosUsuarios(form['column'], form['stringlike'])]
                )

    return jsonify(
            [user.comoDicionario() for user in UserManager().pegarTodosUsuarios()]
        )

@admin.route('/admin/gerenciarusuarios')
def gerenciarUsuarios():
    context = dict()
    return render_template('gerenciarusuarios.html', **context)

@admin.route('/admin/test')
def test():
    return render_template('layout/neo_admin.html')

@admin.route('/admin/test/cadastroproduto')
def testCadastropoduto():
    return render_template('neo_cadastroproduto.html')

@admin.route('/admin/test/gerenciarusuarios')
def testGerenciarUsuarios():
    return render_template('neo_gerenciarusuarios.html')