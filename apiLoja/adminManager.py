from .dbManager import DBManager
from PIL.Image import Image
from uuid import uuid4
from os import path

class AdminManager():
    def __init__(self):
        self.__dbm = DBManager()

    def InsercaoCompletaProduto(self, nome: str, descricao: str, preco: int, quantidade: int, imagem: Image): ...

    def imagemProdutoInserir(self, id: int, image: Image):
        if isinstance(image, Image):
            img_name = path.join('static','prodimages', f'{uuid4()}.webp')
            image.save(img_name, 'WEBP')
            self.__dbm.InserirImagemProduto(id, img_name)
            return img_name
        else:
            raise TypeError(f'{image=} is not Image type')
