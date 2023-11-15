from .userManager import UserManager, validator
from os.path import join as path_join
from flask import Blueprint, request, Response

user = Blueprint('user', __name__)

@user.route('/cadastro', methods=['POST'])
def userCadastro():
    if request.method == 'POST':
        form: dict = request.get_json()

        valido = True
        for i in ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento'):
            if i not in form:
                valido = False

        if valido:
            UserManager().novoUsuario(
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

    return Response(status=500)

@user.route('/login', methods=['POST'])
def userLogin():
    if request.method == 'POST':
        form: dict = request.get_json()

        valido = True
        for i in ('email', 'senha'):
            if not i in form:
                valido = False

        print(form, valido)
        return Response(status=200)

@user.route('/userinfo/<id>', methods=['GET'])
def getUserInfo(id):
    raise NotImplementedError("to be updated")

@user.route('/useraddress/<id>', methods=['GET'])
def getUserAddress(id):
    raise NotImplementedError("to be updated")