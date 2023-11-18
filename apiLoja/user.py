from .userManager import SINGUP_REQUIREMENTS
from .userManager import LOGIN_REQUIREMENTS
from os.path import join as path_join
from .userManager import UserManager
from .userManager import validator
from flask import render_template
from flask import make_response
from flask import Blueprint
from flask import Response
from flask import redirect
from flask import session
from flask import request
from flask import jsonify
from flask import session
from flask import url_for
from flask import flash
from flask import g

user = Blueprint('user', __name__)

@user.route('/cadastro', methods=['GET', 'POST'])
def userCadastro():
    response = make_response(render_template('cadastro.html'))

    if request.method == 'POST':
        if request.content_type.startswith('application/json'):
            form: dict = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = True
        for i in SINGUP_REQUIREMENTS:
            if i not in form:
                valido = False
                break

        if valido:
            code = UserManager().novoUsuario(
                form['email'],
                form['senha'],
                form['nome'],
                form['datanascimento'],
                form['telefone'],
                form['cpf'],
                form['cep'],
                form['rua'],
                form['municipio'],
                form['estado'],
                form['complemento']
            )

            if code == 0:
                flash('Algo deu errado!', 'error')
            else:
                response = redirect(url_for('user.login'))

    return response

@user.route('/login', methods=['GET', 'POST'])
def login():
    response = make_response(render_template('login.html'))
    if request.method == 'POST':
        if request.content_type.startswith('application/json'):
            form: dict = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = True
        for i in LOGIN_REQUIREMENTS:
            if not i in form:
                valido = False

        if valido:
            chaveSessao = UserManager().iniciarSecaoUsuario(
                email=form['email'], senha=form['senha']
            )
            if chaveSessao is not None:
                response = redirect('/')
                response.set_cookie(
                    'usersession', chaveSessao,
                    expires=UserManager().pegarExpiracaoDeSessaoUsuario(chaveSessao)
                    )

                user = UserManager().buscarUsuarioPorEmail(form['email'])
                session['username'] = user.Nome
                session['userid'] = user.idUsuario

    return response


@user.route('/atualizar', methods=['PUT', 'POST'])
def userAtualizar():
    if request.method == 'PUT' or request.method == 'POST':
        form: dict = request.get_json()

        if all (key in form for key in ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento')): ...

@user.route('/userinfo/<id>', methods=['GET'])
def getUserInfo(id):
    if g.userid == int(id):
        email = UserManager().buscarEmailPorUsuarioId(id)
        usuario = UserManager().buscarUsuarioPorEmail(email)
        if usuario != -1:
            return jsonify(**usuario.comoDicionario())
    return Response(404)

@user.route('/useraddress/<id>', methods=['GET'])
def getUserAddress(id):
    return {"objeto":"0"}
    #raise NotImplementedError("to be updated")