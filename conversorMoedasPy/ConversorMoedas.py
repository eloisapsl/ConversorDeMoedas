import requests
import json
def ConverterMoedas(valorOrigem, valorDestino, valorParaConversao):

    url = f'https://economia.awesomeapi.com.br/json/last/{valorOrigem}-{valorDestino}'
    response = requests.get(url)
    
    if response.status_code == 200:
        dados = response.json()
        cotacaoAtual = float(dados[f'{valorOrigem}{valorDestino}']['high'])
        valorConvertido = cotacaoAtual * valorParaConversao
        return valorConvertido
       
    else:
        print(f"Erro na requisição: {response.status_code}")