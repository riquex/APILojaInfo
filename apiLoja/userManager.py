from userManager import UserManager
from hashlib import sha256

class User:
    def __init__(self, idUsuario,Nome, cpf, DataNascimento, telefone, email, validador):
        self.idUsuario = idUsuario
        self.Nome = Nome

def validator(email: str, password: str, key: str):
    return sha256(email.encode() + password.encode() + key.encode()).hexdigest()

class UserManager: ...