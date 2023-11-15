from.dbManager import DBManager
class Produtos:
    def __init__(self, id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        self.id_prod = id_prod
        self.categoria_prod = categoria_prod
        self.nome_prod = nome_prod
        self.desc_prod = desc_prod
        self.quantidade = quantidade
        self.valor_prod = valor_prod
        ProdutosManager.produtos.append(self)  # Adiciona o produto à lista
    
    

class ProdutosManager:
    
    def __init__(self, id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        self.id_prod = id_prod
        self.categoria_prod = categoria_prod
        self.nome_prod = nome_prod
        self.desc_prod = desc_prod
        self.quantidade = quantidade
        self.valor_prod = valor_prod
        ProdutosManager.produtos.append(self)  # Adiciona o produto à lista

    def exibir_informacoes(self):
        print(f"ID do Produto: {self.id_prod}")
        print(f"Categoria do Produto: {self.categoria_prod}")
        print(f"Nome do Produto: {self.nome_prod}")
        print(f"Descrição do Produto: {self.desc_prod}")
        print(f"Quantidade em Estoque: {self.quantidade}")
        print(f"Valor do Produto: R${self.valor_prod:.2f}")

    @staticmethod
    def exibir_todos_produtos():
        for produto in ProdutosManager.produtos:
            ProdutosManager.exibir_informacoes()

    @staticmethod
    def cadastrar_produto(id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod):
        novo_produto = ProdutosManager(id_prod, categoria_prod, nome_prod, desc_prod, quantidade, valor_prod)
        print(f"Produto '{nome_prod}' cadastrado com sucesso!")
        return novo_produto

# Adicionar produtos
ProdutosManager(id_prod=1, categoria_prod='Teclados', nome_prod='Teclado', desc_prod='Teclado mecânico retroiluminado', quantidade=50, valor_prod=150.00)
ProdutosManager(id_prod=2, categoria_prod='Mouses', nome_prod='Mouse', desc_prod='Mouse óptico sem fio', quantidade=30, valor_prod=50.00)
ProdutosManager(id_prod=3, categoria_prod='Monitores', nome_prod='Monitor', desc_prod='Monitor LED 24 polegadas', quantidade=20, valor_prod=300.00)

ProdutosManager.cadastrar_produto(id_prod=4, categoria_prod='Placas de Vídeo', nome_prod='Placa de vídeo', desc_prod='Placa de vídeo potente para jogos', quantidade=15, valor_prod=800.00)
ProdutosManager.cadastrar_produto(id_prod=5, categoria_prod='Placas Mãe', nome_prod='Placa mãe', desc_prod='Placa mãe para processadores modernos', quantidade=10, valor_prod=300.00)

# Exibir produtos
ProdutosManager.exibir_todos_produtos()