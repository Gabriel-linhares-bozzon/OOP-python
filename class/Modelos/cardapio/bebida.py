from item_cardapio import ItemCardapio
class bebidas(ItemCardapio):
    def __init__(self, nome,preco,tamanho):
      super().__init__(nome,preco)
      self._tamanho=tamanho