from .dbManager import DBManager
from typing import Iterable
from PIL.Image import Image
from uuid import uuid4
from os import path
import re

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
    
    def comoLista(self):
        return [
            self.idProduto,
            self.NOME,
            self.Descricao,
            self.Valor,
            self.Quantidade,
            self.staticlink
        ]

    def comoListaEstilizado(self):
        return [
            self.idProduto,
            self.NOME,
            self.truncarDescricao(),
            self.valorEstilizado(),
            self.Quantidade,
            self.staticlink
        ]

    def valorEstilizado(self) -> str:
        text = str(self.Valor)
        text = re.sub(r'\D', '', text)
        if (len(text) > 2):
            left = re.sub(r'\B(?=(\d{3})+(?!\d))', ".", text[:-2])
            right = text[-2:]
            text = f'R${left},{right}'
        return text
    
    def truncarDescricao(self) -> str:
        text = self.Descricao
        if len(text) > 50:
            text = text[:47] + '...'
        return text

class ProdutosManager:
    def __init__(self):
        self.__dbm = DBManager()
    
    def pegarProduto(self, idprod, *args, **kwargs):
        prod = self.__dbm.PegarProdutoCompleto(idProduto=idprod)
        if prod != -1:
            idProduto, nome, Descricao, Valor, Quantidade, staticlink = prod
            return Produto(idProduto, nome, Descricao, Valor, Quantidade, staticlink)
        return -1
    
    def pegarTodosProdutos(self, *args, **kwargs) -> Iterable[Produto]:
        result = self.__dbm.VisualizaProdutosCompletos()
        for prod in result:
            idProduto, nome, Descricao, Valor, Quantidade, staticlink = prod
            yield Produto(idProduto, nome, Descricao, Valor, Quantidade, staticlink)

    def InsercaoCompletaProduto(self, nome: str, descricao: str, preco: int, quantidade: int, imagem: Image):
        if isinstance(imagem, Image):
            img_name = path.join('static','prodimages', f'{uuid4()}.webp')
            imagem.save(img_name, 'WEBP')
            code = self.__dbm.InsercaoCompletaProduto(nome, descricao, preco, 9999999, img_name)
            return code

    def delecaoCompletaProduto(self, prodId):
        return self.__dbm.DelecaoCompletaProduto(prodId)

    def visualizaProdutosCompletosRandom(self) -> Iterable[Produto]:
        result = self.__dbm.VisualizaProdutosCompletosRandom()
        if isinstance(result, (list, tuple)):
            for prod in result:
                yield Produto(*prod)
