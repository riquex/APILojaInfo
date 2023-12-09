from.dbManager import DBManager
class Produto:
    def __init__(self, id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        self.id_prod = id_prod
        self.categoria_prod = categoria_prod
        self.nome_prod = nome_prod
        self.desc_prod = desc_prod
        self.quantidade = quantidade
        self.valor_prod = valor_prod    
    

class ProdutosManager:
    def __init__(self):
        self.__dbm = DBManager()
    
    def PegarProduto(self, idprod, *args, **kwargs):
        return self.__dbm.PegarProdutoCompleto(idProduto=idprod)

    def cadastrar_produto(self, id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        novo_produto = ProdutosManager(id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod)
        print(f"Produto '{nome_prod}' cadastrado com sucesso!")
        return novo_produto
