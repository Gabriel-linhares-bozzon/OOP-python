from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import Bebidas
from Modelos.cardapio.prato import Prato

restaurante2 = Restaurante("Bozzon Grego", "Churrasco", False)
restaurante1 = Restaurante("Bozzon Pizzas", "Massas", True)

restaurante1.receber_avaliacao('Gabriel', 6)
restaurante1.receber_avaliacao('Renata', 8)
restaurante1.receber_avaliacao('Vini', 2)

bebida_coca = Bebidas("Coca-Cola", 5.0, "Grande")
restaurante1.adicinionar_no_cardapio(bebida_coca)

prato_pizza = Prato("Pizza Margherita", 20.0, "Pizza")
restaurante1.adicinionar_no_cardapio(prato_pizza)

def main(): 
   print( restaurante1.exibir_cardapio)    


if __name__ == '__main__':
    main()
