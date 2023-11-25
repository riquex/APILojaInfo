from flask import render_template
from .dbManager import DBManager
from flask import Blueprint
from flask import g

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def indexAdmin():
    return render_template('admin.html')

@admin.route('/admin/cadastroproduto')
def cadastroProduto():
    return render_template('cadastrarproduto.html')

@admin.route('/admin/gerenciarusuarios')
def gerenciarUsuarios():
    context = dict()
    context['datarows'] = DBManager().VisualizarTodosUsuariosCompletos()
    return render_template('gerenciarusuarios.html', **context)