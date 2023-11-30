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

    def VisualizaProdutosCompletos(self):
        self.__cursor.execute("SELECT * FROM ProdutosCompletos")
        return self.__cursor.fetchall()

    def VisualizaProdutosCompletosLimiteCem(self, start):
        self.__cursor.execute(f"SELECT * FROM ProdutosCompletos LIMIT {start}, 100")
        return self.__cursor.fetchall()

    def VisualizaProdutosWhereLikeCompletos(self, column, stringlike):
        self.__cursor.execute(f"SELECT * FROM ProdutosCompletos WHERE {column} LIKE \"%{stringlike}%\"")
        return self.__cursor.fetchall()

    def VisualizaProdutosWhereLikeCompletosLimiteCem(self, column, stringlike, start):
        self.__cursor.execute(f"SELECT * FROM ProdutosCompletos WHERE {column} LIKE \"%{stringlike}%\" LIMIT {start}, 100")
        return self.__cursor.fetchall()

    def VisualizarTodosUsuariosCompletos(self):
        self.__cursor.execute("SELECT * FROM TodosUsuariosCompletos")
        return self.__cursor.fetchall()

    def VisualizarTodosUsuariosCompletosLimiteCem(self, start):
        self.__cursor.execute(f"SELECT * FROM TodosUsuariosCompletos LIMIT {start}, 100")
        return self.__cursor.fetchall()
    
    def VisualizarTodosUsuariosWhereLikeCompletos(self, column, stringlike):
        self.__cursor.execute(f"SELECT * FROM TodosUsuariosCompletos WHERE {column} LIKE \"%{stringlike}%\"")
        return self.__cursor.fetchall()
    
    def VisualizarTodosUsuariosWhereLikeCompletosLimiteCem(self, column, stringlike, start):
        self.__cursor.execute(f"SELECT * FROM TodosUsuariosCompletos WHERE {column} LIKE \"%{stringlike}%\" LIMIT {start}, 100")
        return self.__cursor.fetchall()
    
    def VisualizarUsuariosPorEmail(self, email: str):
        self.__cursor.execute(f'SELECT * FROM todosusuarioscompletos WHERE email LIKE "{email}" LIMIT 1')
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
        self.__cursor.execute(f'SELECT COUNT(*) FROM Usuarios AS u WHERE u.email LIKE "{email}" LIMIT 1')
        return any(self.__cursor.fetchone())

    def InserirUsuario(self, email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.callproc('InsercaoCompletaUsuario', (email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1
    
    def InserirImagem(self, idproduto: int, staticlink: str):
        try:
            self.__cursor.callproc('novaImagem', (idproduto, staticlink))
            self.__mydb.commit()
        except Exception:
            traceback.print_exc()
            return 0
        return 1
    
    def DeletarTodasImagens(self, idproduto: int):
        try:
            self.__cursor.callproc('RemoverTodasImagensDoProduto', (idproduto,))
            self.mydb.commit()
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
        query = f'SELECT validador FROM Usuarios WHERE email LIKE "{email}" LIMIT 1' if email else \
                f'SELECT validador FROM Usuarios WHERE idUsuarios = {idUsuario} LIMIT 1' if idUsuario else None

        if query:
            self.__cursor.execute(query)
            result = self.__cursor.fetchone()
            if result is not None:
                if result[0] == validador:
                    return 1
            return 0
        return 0

    def PegarUsuarioPeloEmail(self, email: str) -> 'int':
        self.__cursor.execute(f'SELECT u.idUsuarios FROM Usuarios AS u WHERE u.email LIKE "{email}" LIMIT 1')
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarEmailPeloUsuarioId(self, UsuarioId: int) -> 'str':
        self.__cursor.execute(f'SELECT u.email FROM Usuarios AS u WHERE u.idUsuarios = {UsuarioId} LIMIT 1')
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarSecaoPeloId(self, idUsuario: int) -> 'str':
        self.__cursor.execute(f'SELECT SU.chaveDaSecao FROM secaousuario AS SU WHERE SU.idUsuario = {idUsuario} LIMIT 1')
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegarExpiracaoPelaSessao(self, sessao: str) -> 'str':
        self.__cursor.execute(f'SELECT SU.timeout FROM secaousuario AS SU WHERE SU.chaveDaSecao LIKE "{sessao}" LIMIT 1')
        result = self.__cursor.fetchone()
        if result is not None:
            return result[0]
        return -1

    def PegerUsuarioCompletoPorSessao(self, sessao: str):
        self.__cursor.execute(f'SELECT idUsuario FROM secaousuario WHERE chaveDaSecao LIKE "{sessao}" LIMIT 1')
        result = self.__cursor.fetchone()
        if result is not None:
            self.__cursor.execute(f'SELECT * FROM todosusuarioscompletos WHERE idUsuarios = {result[0]} LIMIT 1')
            result = self.__cursor.fetchone()
            if result is not None:
                return result
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

    def FinalizarSecaoUsuario(self, idUsuario: int):
        try:
            self.__cursor.callproc('FinalizarSecaoUsuario', (idUsuario,))
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