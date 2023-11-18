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
    
    def VisualizarUsuariosPorEmail(self, email: str):
        self.__cursor.execute("SELECT * FROM todosusuarioscompletos WHERE email LIKE \"%s\"", (email,))
        result = self.__cursor.fetchone()
        if result is not None:
            return result
        return -1

    def VerificarSeUsuarioExiste(self, email: str):
        """Verifica se um usuário existe

        Args:
            email (str): Email do usuário

        Returns:
            bool: Verdadeiro de usuário existir, Falso se não existir
        """        
        self.__cursor.execute('SELECT COUNT(*) FROM Usuarios AS u WHERE u.email LIKE "%s"', (email,))
        return any(self.__cursor.fetchone())

    def InserirUsuario(self, email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.callproc('InsercaoCompletaUsuario', (email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def AtualizacaoCompletaUsuario(self, IdUsuario, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.callproc('AtualizacaoCompletaUsuario', (IdUsuario, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def NovaSecaoDeUsuario(self, IdUsuario: int, chaveDaSecao: str, limite: str):
        try:
            self.__cursor.callproc('NovaSecaoUsuario', (IdUsuario, chaveDaSecao, limite))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def VerificarValidador(self, validador:str, idUsuario:int=None, email:str=None):
        if idUsuario or email:
            if email:
                self.__cursor.execute('SELECT validador FROM Usuarios AS u WHERE u.email LIKE "%s"', (email,))
                result = self.__cursor.fetchone()[0]
                if result == validador:
                    return 1
                return 0
            if idUsuario:
                self.__cursor.execute('SELECT validador FROM Usuarios AS u WHERE u.idUsuarios = %s', (idUsuario,))
                result = self.__cursor.fetchone()[0]
                if result == validador:
                    return 1
                return 0
        return 0

    def PegarUsuarioPeloEmail(self, email: str) -> 'int':
        self.__cursor.execute('SELECT u.idUsuarios FROM Usuarios AS u WHERE u.email LIKE "%s"', (email,))
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarEmailPeloUsuarioId(self, UsuarioId: int) -> 'str':
        self.__cursor.execute('SELECT u.email FROM Usuarios AS u WHERE u.idUsuarios = %s', (UsuarioId,))
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarSecaoPeloId(self, idUsuario: int) -> 'str':
        self.__cursor.execute('SELECT SU.chaveDaSecao FROM secaousuario AS SU WHERE SU.idUsuario = %s', (idUsuario,))
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarExpiracaoPelaSessao(self, sessao: str) -> 'str':
        self.__cursor.execute('SELECT SU.timeout FROM secaousuario AS SU WHERE SU.chaveDaSecao LIKE "%s"', (sessao,))
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def LimparCarrinho(self, idUsuario: int):
        try:
            self.__cursor.callproc("LimparCarrinho", (idUsuario,))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def InserirOuAtualizarCarrinho(self, idUsuario: int, idProduto: int, quantidade: int):
        try:
            self.__cursor.callproc("InserirOuAtualizarCarrinho", (idUsuario, idProduto, quantidade))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1

    def InsercaoCompletaProduto(self, nome: str, descricao: str, preco: int, quantidade: int):
        try:
            self.__cursor.execute("InsercaoCompletaProduto", (nome, descricao, preco, quantidade))
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