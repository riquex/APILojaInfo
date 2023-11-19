import uuid
from hashlib import sha256
from .dbManager import DBManager
from datetime import datetime, timedelta

SINGUP_REQUIREMENTS = ('email', 'senha', 'nome', 'datanascimento', 'telefone', 'cpf', 'cep', 'rua', 'municipio', 'estado', 'complemento')
LOGIN_REQUIREMENTS = ('email', 'senha')

def validator(email: str, password: str, key: str):
    return sha256(email.encode() + password.encode() + key.encode()).hexdigest()

class User:
    def __init__(self, idUsuario, email, validador,Nome, DataNascimento, telefone, cpf, cep, rua, municipio, estado, complemento):
        self.idUsuario = idUsuario
        self.Nome = Nome
        self.cpf = cpf
        self.DataNascimento = DataNascimento
        self.telefone = telefone
        self.email = email
        self.validador = validador
        self.cep = cep
        self.rua = rua
        self.municipio = municipio
        self.estado = estado
        self.complemento = complemento
        self.logado = False

    def comoDicionario(self):
        return {
            'idUsuario': self.idUsuario,
            'nome': self.Nome,
            'cpf': self.cpf,
            'dataNascimento': self.DataNascimento,
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
            self, email,  senha, Nome,
            DataNascimento, Telefone, cpf,
            cep, rua, municipio, estado,
            complemento, *args, **kwargs):
        validador = validator(email, senha, '42')
        return self.__dbm.InserirUsuario(
            email, validador, Nome, DataNascimento,
            Telefone, cpf, cep, rua, municipio, estado, complemento
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

    def buscarEmailPorUsuarioId(self, idUsuario: int):
        return self.__dbm.PegarEmailPeloUsuarioId(idUsuario)

    def finalizarSecaoUsuario(self, idUsuario: int):
        code = self.__dbm.FinalizarSecaoUsuario(idUsuario)
        return code

if __name__ == '__main__': # Testes
    a = UserManager()
    print(a.IniciarSecaoUsuario("jdudmarsh8@wordpress.com", "$2a$04$KdsWiQ/t.X4/pO33WzrbFuYcb7DnfbA3UIK15nzzOcDz0Op1bOkFi", 2400))