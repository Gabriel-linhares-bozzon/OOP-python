'''Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.'''
class Restaurante :
    def __init__(self,nome,categoria,status,expecialidade,ano):
        self.nome = nome
        self.categoria = categoria
        self.status = status
        self.expecialidade = expecialidade
        self.ano = ano  
        

Restaurante1=Restaurante(nome='Pizza do Bozzon', categoria='Pizzaria',status='ativo',expecialidade='Pizza de calabresa',ano='1997')