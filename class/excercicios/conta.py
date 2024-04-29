
class Conta:
    def __init__(self): #Função construtora 
        print("Construindo objeto...{}".format(self))
        self.numero = numero
        self.titular =titular
        self.saldo = saldo
        self.limite = limite 

    def extrato(self):
        print("Sr ou Sra {}\nO Seu saldo é{}".format(self.titular,self.saldo))
                