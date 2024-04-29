from Modelos.avaliacao import Avaliacao
from Modelos.cardapio.item_cardapio import ItemCardapio
class Restaurante:
    restaurantes = []
    
    def __init__(self,nome,categoria,status):
        self.nome=nome.title()
        self.categoria=categoria.upper()
        self._status=status
        self._avaliacao = []
        self._cardapio= []
        Restaurante.restaurantes.append(self)#Criando os proprios metodos

    def __str__(self):#Metodos especiais 5
        return f' {self.nome}|{self.categoria} '
    
    @classmethod
    def listar_restaurantes(cls):#Listagem dos restaurantes atraves de um metodo/funcao
        print(f'{'Nome do restaurante:'.ljust(26)}|{'categoria:'.ljust(26)}|{'Status:'.ljust(26)}|{'Avaliação:'.ljust(24)}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} |{restaurante.categoria.ljust(25)} |{restaurante.status.ljust(25)} |{str(restaurante.media_avaliacoes).ljust(25)}')

    @property   
    def status(self):
        return 'True ' if self._status else 'False' # vai alterar o atributo e alterar
    
    def alternar_estado(self):
        self._status = not self._status

    def receber_avaliacao(self, cliente,nota):
        avaliacao=Avaliacao(cliente,nota)
        self._avaliacao.append(avaliacao)
    @property
    def media_avaliacoes(self): 
         if not self._avaliacao:
             return '-'
         soma_das_notas = sum(int(avaliacao._nota) for avaliacao in self._avaliacao)
         quantidades_de_notas = len(self._avaliacao)
         media=round((soma_das_notas/quantidades_de_notas)/2,1)
         return media

    def adicinionar_no_cardapio(self,item):
        if isinstance(item,ItemCardapio):
            self._cardapio.append(item)