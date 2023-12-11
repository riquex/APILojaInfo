from .userManager import SINGUP_REQUIREMENTS
from .userManager import UPDATE_REQUIREMENTS
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
from flask import abort
from flask import flash
from flask import g

user = Blueprint('user', __name__)

@user.route('/cadastro/massivo', methods=["POST"])
def userCadastroMassivo():
    if g.admin != True: abort(404)
    if request.method == 'POST':
        code = 0
        size = 0
        um = UserManager()

        if request.content_type.startswith('application/json'):
            form: dict|list[dict] = request.get_json()
            print(type(form))
        else:
            form = dict()

        response = Response(status=201)

        if isinstance(form, list):
            size = len(form)
            for row in form:
                valido = all(key in row for key in SINGUP_REQUIREMENTS)
                if valido:
                    code += um.novoUsuario(**row)
        if code != size:
            response = Response(status=400)
        return response
    return Response(status=404)

@user.route('/cadastro', methods=['GET', 'POST'])
def userCadastro():
    response = make_response(render_template('cadastro.html'))

    if request.method == 'POST':
        response = Response(status='201')
        if request.content_type.startswith('application/json'):
            form: dict | list[dict] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = False
        if isinstance(form, dict):
            valido = all(key in form for key in SINGUP_REQUIREMENTS)

        if valido:
            try:
                valid_data = \
                    3 < len(form['cep']) <= 8 and \
                    3 < len(form['cpf']) <= 45 and \
                    3 < len(form['email']) <= 128 and \
                    3 < len(form['nome']) <= 128 and \
                    3 < len(form['datanascimento']) <= 45 and \
                    3 < len(form['rua']) <= 128 and \
                    3 < len(form['municipio']) <= 45 and \
                    3 < len(form['estado']) <= 45 and \
                    len(form['complemento']) <= 45 and \
                    3 < len(form['telefone']) <= 128 and \
                    3 < len(form['senha'])

                print(valid_data)
                if valid_data:
                    response.status = "201"
                    code = UserManager().novoUsuario(**form)
                    if code == 0:
                        response.status = "400"
                    else:
                        response = redirect(url_for('user.login'), code=201)
                else:
                    response.status = "400"
            except: pass

        else:
            response.status = "400"

    return response

@user.route('/user/atualizarusuario', methods=['PUT'])
def atulizarusuario():
    response = make_response(render_template('notfound.html'))
    if request.method == 'PUT':
        response = Response(status='201')
        if request.content_type.startswith('application/json'):
            form: dict | list[dict] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()

        valido = all(key in form for key in UPDATE_REQUIREMENTS)
        if valido:
            if g.admin == True or g.userid == int(form['idUsuarios']):
                code = UserManager().atualizarUsuario(**form)
                if code == 0:
                    response.status = 400
    return response

@user.route('/user/delecaousuario', methods=['DELETE'])
def delecaoUsuario():
    response = make_response(render_template('notfound.html'))
    if request.method == 'DELETE':
        response = Response(status='201')
        if request.content_type.startswith('application/json'):
            form: dict | list[dict] = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()
        
        valido = all(key in form for key in ('idUsuarios',))
        if valido:
            if g.admin == True or g.userid == int(form['idUsuarios']):
                code = UserManager().delecaoCompletaUsuario(form['idUsuarios'])
                if code == 0:
                    response.status = 500
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
    userManager = UserManager()
    response = make_response(render_template('login.html'))
    response.status = "200"

    cookies = request.cookies
    if 'usersession' in cookies:
        user = userManager.buscarUsuarioPorSessao(cookies['usersession'])
        if user != -1:
            session['username'] = user.Nome
            session['userid'] = user.idUsuarios
            if userManager.verificarSeEhAdmin(user.idUsuarios) == 1:
                session['admin'] = True
            response = redirect(url_for('loja.index'))
            print('loja.index')
            return response
        else:
            response.set_cookie('usersession', '', expires=0)

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
            chaveSessao = userManager.iniciarSecaoUsuario(
                email=form['email'], senha=form['senha']
            )
            if chaveSessao is not None:
                response = redirect('/')
                response.set_cookie(
                    'usersession', chaveSessao,
                    expires=userManager.pegarExpiracaoDeSessaoUsuarioDateTime(chaveSessao)
                    )

                user = userManager.buscarUsuarioPorEmail(form['email'])
                session['username'] = user.Nome
                session['userid'] = user.idUsuarios
                print(f'admin test: {userManager.verificarSeEhAdmin(user.idUsuarios)}')
                if userManager.verificarSeEhAdmin(user.idUsuarios) == 1:
                    session['admin'] = True
            else:
                response = Response(status=400)

    return response

@user.route('/userinfo/<id>', methods=['GET'])
def getUserInfo(id):
    if g.userid == int(id) or g.admin == True:
        email = UserManager().buscarEmailPorUsuarioId(id)
        usuario = UserManager().buscarUsuarioPorEmail(email)
        if usuario != -1:
            return jsonify(**usuario.comoDicionario())
    abort(404)