import uuid
from hashlib import sha256
from dbManager import DBManager
from datetime import datetime, timedelta

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
        self.comoplemento = complemento

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
            'complemento': self.comoplemento
        }

class UserManager:
    def __init__(self) -> None:
        self.__dbm = DBManager()

    def IniciarSecaoUsuario(self, email: str, senha: str, horasLimite:int=24):
        validador = validator(email, senha, '42')
        if self.__dbm.VerificarValidador(email=email, validador=validador):# or True:
            limite = datetime.now() + timedelta(hours=horasLimite)
            strLimite = limite.strftime('%Y-%m-%d %H:%M:%S')

            chaveSecao = uuid.uuid4()
            idUsuario = self.__dbm.PegarUsuarioPeloEmail(email=email)

            if idUsuario == -1:
                raise ValueError(f'There is no user with {email =}')

            return self.__dbm.NovaSecaoDeUsuario(idUsuario, chaveSecao.hex, strLimite)
        return -1

if __name__ == '__main__': # Testes
    a = UserManager()
    print(a.IniciarSecaoUsuario("jdudmarsh8@wordpress.com", "$2a$04$KdsWiQ/t.X4/pO33WzrbFuYcb7DnfbA3UIK15nzzOcDz0Op1bOkFi", 2400))