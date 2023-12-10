from .dbManager import DBManager
from typing import Iterable

class Produto:
    def __init__(self, idProduto, NOME, Descricao, Valor, Quantidade, staticlink):
        self.idProduto = idProduto
        self.NOME = NOME
        self.Descricao = Descricao
        self.Valor = Valor
        self.Quantidade = Quantidade
        self.staticlink = staticlink

    def comoDicionario(self):
        return {
            "idProduto":    self.idProduto,
            "NOME":         self.NOME,
            "Descricao":    self.Descricao,
            "Valor":        self.Valor,
            "Quantidade":   self.Quantidade,
            "staticlink":   self.staticlink,
        }

class ProdutosManager:
    def __init__(self):
        self.__dbm = DBManager()
    
    def pegarProduto(self, idprod, *args, **kwargs):
        prod = self.__dbm.PegarProdutoCompleto(idProduto=idprod)
        if prod != -1:
            idProduto, nome, Descricao, Valor, Quantidade, staticlink = prod
            return Produto(idProduto, nome, Descricao, Valor, Quantidade, staticlink)
        return prod
    
    def pegarTodosProdutos(self, *args, **kwargs) -> Iterable[Produto]:
        result = self.__dbm.VisualizaProdutosCompletos()
        for prod in result:
            idProduto, nome, Descricao, Valor, Quantidade, staticlink = prod
            yield Produto(idProduto, nome, Descricao, Valor, Quantidade, staticlink)

    def cadastrar_produto(self, id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        novo_produto = ProdutosManager(id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod)
        print(f"Produto '{nome_prod}' cadastrado com sucesso!")
        return novo_produto
