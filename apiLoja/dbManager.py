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