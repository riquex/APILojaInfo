import os
import traceback
import mysql.connector
from dotenv import load_dotenv

load_dotenv(
    dotenv_path=os.path.join(
            os.path.dirname(__file__),
            '..',
            '.env'
        )
    )

class DBManager:
    def __init__(self) -> None:
        self.__mydb = mysql.connector.connect(
            host=       os.environ.get('host'),
            user=       os.environ.get('user'),
            password=   os.environ.get('password'),
            database=   os.environ.get('database')
        )
        self.__cursor = self.__mydb.cursor()

    def VisualizaCompras(self):
        self.__cursor.execute("SELECT * FROM `todascompras`")
        return self.__cursor.fetchall()

    def VisualizarCarrinhoPreco(self):
        self.__cursor.execute("SELECT * FROM carrinhopreco")
        return self.__cursor.fetchall()

    def VisualizarTodosUsuariosCompletos(self):
        self.__cursor.execute("SELECT * FROM TodosUsuariosCompletos")
        return self.__cursor.fetchall()

    def VerificarSeUsuarioExiste(self, email: str):
        """Verifica se um usuário existe

        Args:
            email (str): Email do usuário

        Returns:
            bool: Verdadeiro de usuário existir, Falso se não existir
        """        
        self.__cursor.execute(f'SELECT COUNT(*) FROM Usuarios AS u WHERE u.email LIKE "{email}"')
        return any(self.__cursor.fetchone())

    def InserirUsuario(self, email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.execute(f"CALL InsercaoCompletaUsuario({email}, {validador}, {Nome}, {DataNascimento}, {Telefone}, {cpf}, {cep}, {rua}, {municipio}, {estado}, {complemento})")
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def AtualizacaoCompletaUsuario(self, IdUsuario, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.execute(f"CALL AtualizacaoCompletaUsuario({IdUsuario}, {Nome}, {DataNascimento}, {Telefone}, {cpf}, {cep}, {rua}, {municipio}, {estado}, {complemento})")
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def NovaSecaoDeUsuario(self, IdUsuario, chaveDaSecao, limite):
        try:
            self.__cursor.execute(f'CALL NovaSecaoUsuario({IdUsuario}, "{chaveDaSecao}", "{limite}")')
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def VerificarValidador(self, validador:str, idUsuario:int=None, email:str=None):
        if idUsuario or email:
            if email:
                self.__cursor.execute(f'SELECT validador FROM Usuarios AS u WHERE u.email LIKE "{email}"')
                result = self.__cursor.fetchone()[0]
                if result == validador:
                    return 1
                return 0
            if idUsuario:
                self.__cursor.execute(f'SELECT validador FROM Usuarios AS u WHERE u.idUsuarios = {idUsuario}')
                result = self.__cursor.fetchone()[0]
                if result == validador:
                    return 1
                return 0
        return 0

    def PegarUsuarioPeloEmail(self, email: str) -> 'int':
        self.__cursor.execute(f'SELECT u.idUsuarios FROM Usuarios AS u WHERE u.email LIKE "{email}"')
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def LimparCarrinho(self, idUsuario: int):
        try:
            self.__cursor.execute(f"CALL LimparCarrinho({idUsuario})")
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def InserirOuAtualizarCarrinho(self, idUsuario: int, idProduto: int, quantidade: int):
        try:
            self.__cursor.execute(f"CALL InserirOuAtualizarCarrinho({idUsuario}, {idProduto}, {quantidade})")
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def InsercaoCompletaProduto(self, nome: str, descricao: str, preco: int, quantidade: int):
        try:
            self.__cursor.execute(f"CALL InsercaoCompletaProduto({nome}, {descricao}, {preco}, {quantidade})")
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

if __name__ == '__main__':
    a = DBManager()
    print(a)
    print(len(a.VisualizarTodosUsuariosCompletos()))
    print(a.VerificarSeUsuarioExiste('dshackletonrp@homestead.com'))
    print(a.VerificarValidador(validador='$2a$04$DhDuIuoKjTQ0GAOK.uarGejPWoDhZg5UqPiGx9SUEyfRWchLC8GDy'))
    print(a.PegarUsuarioPeloEmail('jdudmarsh8@wordpress.com'))