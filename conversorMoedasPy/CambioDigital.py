import ConversorMoedas
from datetime import date


def main():
    moedas = {1:"BRL", 2:"USD", 3:"EUR"}
    while True:
        print("---------------------------------\n")
        print("      CONVERSOR DE MOEDAS\n")
        print("---------------------------------\n")
        print("1. BRL (Real Brasileiro)\n")
        print("2. USD (Dólar Americano)\n")
        print("3. EUR (Euro)\n")
        
        
        # Coleta dados de entrada e verifica se são válidos ou não
        while True:
            valorOrigem = input("Moeda de origem:\n")
            if valorOrigem != "1" and valorOrigem != "2" and valorOrigem != "3":
                print("Opcão inválida. Tente novamente.")
            else:
                break;
            
        while True:
            valorDestino = input("Moeda de destino:\n")
            if valorDestino != "1"and valorDestino != "2" and valorDestino != "3":
                print("Opcao invalida. Tente novamente.")
            elif valorOrigem == valorDestino:
                print("ERRO: Não é possivel converter moedas iguais. Selecione outra moeda para conversão.")
            else:
                break;
        
        valorOrigemInt = int(valorOrigem)
        valorDestinoInt = int(valorDestino)
        
        valorParaConversao = float(input("Valor a ser convertido: "))
    
        valorConvertido = ConversorMoedas.ConverterMoedas(moedas[valorOrigemInt], moedas[valorDestinoInt], valorParaConversao)
        print(f"{valorParaConversao:.2f} {moedas[valorOrigemInt]} correspondem a {valorConvertido:.2f} {moedas[valorDestinoInt]} no dia", date.today())
        
        
        while True:
            opcao = input("Deseja realizar outra conversão?\n1.Sim\n2.Não ")
            if opcao == "2":
                print("Até mais!\n")
                exit()
            elif opcao == "1":
                break
        

    
if __name__ == "__main__":
  main()
