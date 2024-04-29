# 5) Crie uma classe chamada `Cliente` e pense em 4 atributos. Em seguida, instancie 3 objetos desta classe e atribua valores aos seus atributos através de um método construtor.
class Cliente():
    def __init__(self,nome='',idade=0,email='',telefone=''):
        self.nome= nome,
        self.idade=idade,
        self.email=email,
        self.telefone=telefone,

    # Instanciando três objetos da classe Cliente e atribuindo valores aos seus atributos através do construtor
cliente1 = Cliente(nome='Alice', idade=25, email='alice@gmail.com', telefone='123-456-7890')
cliente2 = Cliente(nome='Bob', idade=30, email='bob@gmail.com', telefone='987-654-3210')
cliente3 = Cliente(nome='Charlie', idade=22, email='charlie@gmail.com', telefone='555-123-4567')

print(cliente1.nome,"\n",
      cliente2.nome,"\n",
      cliente3.nome,"\n")