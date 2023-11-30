from datetime import datetime, timedelta
from .dbManager import DBManager
from typing import Iterable
from hashlib import sha256
import uuid

SINGUP_REQUIREMENTS = ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento')
LOGIN_REQUIREMENTS = ('email', 'senha')

def validator(email: str, password: str, key: str):
    return sha256(email.encode() + password.encode() + key.encode()).hexdigest()

class User:
    def __init__(self, idUsuario, email, validador, Nome, datanascimento, telefone, cpf, cep, rua, municipio, estado, complemento):
        self.idUsuario: int = idUsuario
        self.Nome: str = Nome
        self.cpf: str = cpf
        self.datanascimento: str | datetime = datanascimento
        self.telefone: str = telefone
        self.email: str = email
        self.validador: str = validador
        self.cep: str = cep
        self.rua: str = rua
        self.municipio: str = municipio
        self.estado: str = estado
        self.complemento: str = complemento
        self.logado = False

    def comoDicionario(self):
        return {
            'idUsuario': self.idUsuario,
            'nome': self.Nome,
            'cpf': self.cpf,
            'dataNascimento': self.datanascimento,
            'telefone': self.telefone,
            'email': self.email,
            'validor': self.validador,
            'cep': self.cep,
            'rua': self.rua,
            'municipio': self.municipio,
            'estado': self.estado,
            'complemento': self.complemento
        }

class UserManager:
    def __init__(self) -> None:
        self.__dbm = DBManager()

    def novoUsuario(
            self, email,  senha, nome,
            datanascimento, telefone, cpf,
            cep, rua, municipio, estado,
            complemento, *args, **kwargs):
        validador = validator(email, senha, '42')
        return self.__dbm.InserirUsuario(
            email, validador, nome, datanascimento,
            telefone, cpf, cep, rua, municipio, estado, complemento
        )

    def iniciarSecaoUsuario(self, email: str, senha: str, horasLimite:int=24):
        validador = validator(email, senha, '42')
        if self.__dbm.VerificarValidador(email=email, validador=validador):# or True:
            limite = datetime.now() + timedelta(hours=horasLimite)
            strLimite = limite.strftime('%Y-%m-%d %H:%M:%S')

            chaveSecao = uuid.uuid4()
            idUsuario = self.__dbm.PegarUsuarioPeloEmail(email=email)

            if idUsuario == -1:
                raise ValueError(f'There is no user with {email =}')

            _code = self.__dbm.NovaSecaoDeUsuario(idUsuario, chaveSecao.hex, strLimite)

            return self.__dbm.PegarSecaoPeloId(self.__dbm.PegarUsuarioPeloEmail(email))
        return None

    def pegarExpiracaoDeSessaoUsuario(self, sessao: str):
        return self.__dbm.PegarExpiracaoPelaSessao(sessao)

    def pegarExpiracaoDeSessaoUsuarioDateTime(self, sessao: str):
        expiracao = self.__dbm.PegarExpiracaoPelaSessao(sessao)
        result = datetime.strptime(expiracao, '%Y-%m-%d %H:%M:%S')
        return result

    def buscarUsuarioPorEmail(self, email: str):
        result = self.__dbm.VisualizarUsuariosPorEmail(email=email)
        if result != -1:
            idUsuario, Nome, DataNascimento, Telefone, cpf, email, cep, rua, municipio, estado, complemento = result
            usuario = User(idUsuario, email, '', Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento)
            return usuario
        return -1
    
    def buscarUsuarioPorSessao(self, sessao: str):
        result = self.__dbm.PegerUsuarioCompletoPorSessao(sessao)
        if result != -1:
            idUsuario, Nome, DataNascimento, Telefone, cpf, email, cep, rua, municipio, estado, complemento = result
            usuario = User(idUsuario, email, '', Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento)
            return usuario
        return -1

    def pegarTodosUsuarios(self, column='', stringlike='', start=-1) -> Iterable[User]:
        if column and stringlike:
            if start > -1:
                resultado_busca = self.__dbm.VisualizarTodosUsuariosWhereLikeCompletosLimiteCem(column, stringlike, start)
            else:
                resultado_busca = self.__dbm.VisualizarTodosUsuariosWhereLikeCompletos(column, stringlike)
        elif column and start > -1:
            resultado_busca = self.__dbm.VisualizarTodosUsuariosCompletosLimiteCem(start)
        else:
            resultado_busca = self.__dbm.VisualizarTodosUsuariosCompletos()

        for userData in resultado_busca:
            idUsuario, Nome, DataNascimento, Telefone, cpf, email, cep, rua, municipio, estado, complemento = userData
            usuario = User(idUsuario, email, '', Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento)
            yield usuario

    def buscarEmailPorUsuarioId(self, idUsuario: int):
        return self.__dbm.PegarEmailPeloUsuarioId(idUsuario)

    def finalizarSecaoUsuario(self, idUsuario: int):
        code = self.__dbm.FinalizarSecaoUsuario(idUsuario)
        return code