from Modelos.restaurante import Restaurante
from Modelos.cardapio.bebida import bebidas
from Modelos.cardapio.prato import Prato

restaurante2=Restaurante("Bozzon Grego","Churrasco","False");
restaurante1=Restaurante("Bozzon Pizzas","Massas","true");

restaurante1.receber_avaliacao('Gabriel','6')
restaurante1.receber_avaliacao('Renata','8')
restaurante1.receber_avaliacao('Vini','2')
#restaurante_praca.adicinionar_no_cardapio()

def main(): 
    Restaurante.listar_restaurantes()
    


if __name__ == '__main__':
    main()
        