from flask import Blueprint
from flask import render_template

admin = Blueprint('admin', __name__)

@admin.route('/admin')
def indexAdmin():
    return render_template('admin.html')

@admin.route('/admin/cadastroproduto')
def cadastroProdutos():
    return render_template('cadastrarproduto.html')