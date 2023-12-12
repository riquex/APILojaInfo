import mysql.connector
from datetime import datetime

class VendaManager:
    def __init__(self, idvendas, datavenda, idProd, valorprod, valortotal, enderecodaentrega, idusuario, nomeusuario):
        self.idvendas = idvendas
        self.datavenda = datavenda
        self.idProd = idProd
        self.valorprod = valorprod
        self.valortotal = valortotal
        self.enderecodaentrega = enderecodaentrega
        self.idusuario = idusuario
        self.nomeusuario = nomeusuario

    def cadastrar_venda(self):
        try:
            conn = mysql.connector.connect(
                host='db4free.net',
                user='projetofinalkb',
                password='projetofinalkb',
                database='projetofinalkb'
            )

            cursor = conn.cursor()

            # Chama a procedure 'NovaVenda' com os valores como parâmetros
            cursor.callproc('NovaVenda', (
                self.idvendas,
                self.datavenda,
                self.idProd,
                self.valorprod,
                self.valortotal,
                self.enderecodaentrega,
                self.idusuario,
                self.nomeusuario
            ))

            # Faz o commit para salvar as alterações no banco de dados
            conn.commit()

            print("Venda cadastrada com sucesso!")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")

        finally:
            # Fecha o cursor e a conexão
            if 'cursor' in locals() and cursor is not None:
                cursor.close()
            if 'conn' in locals() and conn.is_connected():
                conn.close()

# Exemplo de uso da classe
if __name__ == '__main__':
    data_venda = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    venda = VendaManager(1, data_venda, 101, 50.0, 150.0, 'Rua A, 123', 1, 'Alexandre')

    venda.cadastrar_venda()