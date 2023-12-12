from .produtosManager import ProdutosManager
from .dbManager import DBManager

class LojaManager:
    def __init__(self) -> None:
        self.__dbm = DBManager()
    
    def listaAleatoriaDeProdutos(self):
        result = ProdutosManager().visualizaProdutosCompletosRandom()
        return [prod.comoListaEstilizado() for prod in result]

    def adicionarAoCarrinho(self, idCliente, idProduto, quantidade, *args, **kwdargs):
        return self.__dbm.AdicionarAoCarrinho(idCliente, idProduto, quantidade)

    def removerItemdoCarrinho(self, idCliente, idProduto, *args, **kwdargs):
        return self.__dbm.DeletarItemCarrinho(idCliente, idProduto, )

    def limparCarrinho(self, idCliente, *args, **kwdargs):
        return self.__dbm.DeletarTodosItensCarrinho(idCliente)

    def pegarCarrinhoDoCliente(self, idCliente, *args, **kwdargs):
        result = self.__dbm.VisualizarCarrinhoDoUsuario(idCliente)
        return result