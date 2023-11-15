from userManager import UserManager
from hashlib import sha256

class UserManager:
    def __init__(self, idUsuario,Nome, cpf, DataNascimento, telefone, email, validador):
        self.idUsuario = idUsuario
        self.Nome = Nome
        self.cpf = cpf
        self.DataNascimento = DataNascimento
        self.telefone = telefone
        self.email = email
        self.validador = validador
    
    def comoDicionario(self):
        return {
            'idUsuario': self.idUsuario,
            'nome': self.Nome,
            'cpf': self.cpf,
            'dataNascimento': self.DataNascimento,
            'telefone': self.telefone,
            'email': self.email,
            'validor': self.validador
        }

def validator(email: str, password: str, key: str):
    return sha256(email.encode() + password.encode() + key.encode()).hexdigest()

class UserManager: ...