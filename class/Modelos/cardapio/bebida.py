from .item_cardapio import ItemCardapio

class Bebidas(ItemCardapio):  # Alterei o nome da classe para começar com maiúscula, conforme convenção PEP8
    def __init__(self, nome, preco, tamanho):
        super().__init__(nome, preco)
        self._tamanho = tamanho
