import traceback
import mysql.connector

class DBManager:
    def __init__(self) -> None:
        self.__mydb = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="alunolab",
            database="projetofinalkb"
        )
        self.__cursor = self.__mydb.cursor()
    
    def VisualizaCompras(self):
        self.__cursor.execute("SELECT * FROM `todascompras`")
        return self.__cursor.fetchall()
    
    def InserirUsuario(self, email, validador, Nome, DataNascimento, Telefone, cpf, cep, rua, municipio, estado, complemento):
        try:
            self.__cursor.execute(f"CALL InsercaoCompletaUsuario({email}, {validador}, {Nome}, {DataNascimento}, {Telefone}, {cpf}, {cep}, {rua}, {municipio}, {estado}, {complemento})")
            self.__mydb.commit()
        except Exception as e:
            traceback.print_tb()

if __name__ == '__main__':
    a = DBManager()
    print(a)
    print(a.VisualizaCompras())