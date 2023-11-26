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

@user.route('/cadastro/massivo', methods=["POST"])
def userCadastroMassivo():
    if request.method == 'POST':
        code = 0
        um = UserManager()

        if request.content_type.startswith('application/json'):
            form: dict|list[dict] = request.get_json()
            print(type(form))
        else:
            form = dict()

        response = make_response(str(form))
        response.status = '200'

        if isinstance(form, list):
            for row in form:
                valido = all(key in SINGUP_REQUIREMENTS for key in row)
                if valido:
                    code += um.novoUsuario(**row)
        if code != 0:
            response.status = '409'
        return response
    return redirect('/')

@user.route('/cadastro', methods=['GET', 'POST'])
def userCadastro():
    response = make_response(render_template('cadastro.html'))

    if request.method == 'POST':
        if request.content_type.startswith('application/json'):
            form: dict | list[dict] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = True
        if isinstance(form, dict):
            valido = all(key in SINGUP_REQUIREMENTS for key in form)
        else: valido = False

        if valido:
            code = UserManager().novoUsuario(**form)

            if code == 0:
                flash('Algo deu errado!', 'error')
                response.status = "409"
            else:
                response = redirect(url_for('user.login'), code=201)
        else:
            response.status = "409"

    return response

@user.route('/logoff', methods=['GET', 'POST'])
def logoff():
    response = redirect('/')
    response.set_cookie('usersession', '', expires=0)
    if 'userid' in session:
        UserManager().finalizarSecaoUsuario(session['userid'])
    session.clear()
    return response

@user.route('/login', methods=['GET', 'POST'])
def login():
    response = make_response(render_template('login.html'))

    cookies = request.cookies
    if 'usersession' in cookies:
        user = UserManager().buscarUsuarioPorSessao(cookies['usersession'])
        if user != -1:
            session['username'] = user.Nome
            session['userid'] = user.idUsuario
            response = redirect('/')
            return response

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
                    expires=UserManager().pegarExpiracaoDeSessaoUsuarioDateTime(chaveSessao)
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