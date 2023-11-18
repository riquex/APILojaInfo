from .userManager import UserManager, validator
from os.path import join as path_join
from flask import Blueprint, request, Response, jsonify, make_response, redirect, render_template

user = Blueprint('user', __name__)

@user.route('/cadastro', methods=['GET', 'POST'])
def userCadastro():
    return render_template('cadastro.html')

@user.route('/authenticate/cadastro', methods=['POST'])
def userAuthenticateCadastro():
    if request.method == 'POST':
        print(request.content_type)
        if request.content_type.startswith('application/json'):
            form: dict = request.get_json()
        elif request.content_type.startswith('application/x-www-form-urlencoded'):
            form = request.form
        else:
            form = dict()
        print(form)

        valido = True
        for i in ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento'):
            if i not in form:
                valido = False

        if valido and False:
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
    

    response = redirect('/login')
    return response

@user.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@user.route('/authenticate/login', methods=['POST'])
def userAuthenticateLogin():
    if request.method == 'POST':
        form: dict = request.get_json()

        valido = True
        for i in ('email', 'senha'):
            if not i in form:
                valido = False
        if valido:
            chaveSessao = UserManager().iniciarSecaoUsuario(
                email=form['email'], senha=form['senha']
            )

            response = redirect('/')
            response.set_cookie(
                'usersession', chaveSessao,
                expires=UserManager().pegarExpiracaoDeSessaoUsuario(chaveSessao)
                )
            return response
    return Response(500)

@user.route('/atualizar', methods=['PUT', 'POST'])
def userAtualizar():
    if request.method == 'PUT' or request.method == 'POST':
        form: dict = request.get_json()

        if all (key in form for key in ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento')): ...

@user.route('/userinfo/<id>', methods=['GET'])
def getUserInfo(id):
    email = UserManager().buscarEmailPorUsuarioId(id)
    usuario = UserManager().buscarUsuarioPorEmail(email)
    if usuario != -1:
        return jsonify(**usuario.comoDicionario())
    return Response(404)

@user.route('/useraddress/<id>', methods=['GET'])
def getUserAddress(id):
    return {"objeto":"0"}
    #raise NotImplementedError("to be updated")