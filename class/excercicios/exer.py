'''Em uma carreira de desenvolvimento de software, a prática consistente desempenha um papel fundamental na construção de bases sólidas. Pensando nisso, criamos uma lista de atividades (não obrigatórias) focada em prática para melhorar ainda mais sua experiência de aprendizagem.

Bora praticar então?


Exercícios
Implemente uma classe chamada Carro com os atributos básicos, como modelo, cor e ano. Crie uma instância dessa classe e atribua valores aos seus atributos.
Crie uma classe chamada Restaurante com os atributos nome, categoria, ativo e crie mais 2 atributos. Instancie um restaurante e atribua valores aos seus atributos.
Modifique a classe Restaurante adicionando um construtor que aceita nome e categoria como parâmetros e inicia ativo como False por padrão. Crie uma instância utilizando o construtor.
Adicione um método especial __str__ à classe Restaurante para que, ao imprimir uma instância, seja exibida uma mensagem formatada com o nome e a categoria. Exiba essa mensagem para uma instância de restaurante.
Crie uma classe chamada Cliente e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.'''
class Carro (object):
    def __init__(self,modelo,cor,ano,valores,marcas):
        self.modelo = modelo
        self.cor = cor
        self.ano= ano
        self.valores= valores
        self.marcas = marcas

    def value(self, modelo):
        return print('O modelo do carro é:${modelo},\n ')
        
        
