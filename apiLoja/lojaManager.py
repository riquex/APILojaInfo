from .produtosManager import ProdutosManager
from .dbManager import DBManager

class LojaManager:
    def __init__(self) -> None:
        self.__dbm = DBManager()
    
    def listaAleatoriaDeProdutos(self):
        result = ProdutosManager().visualizaProdutosCompletosRandom()
        return [prod.comoListaEstilizado() for prod in result]