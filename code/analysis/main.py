import pandas as pd
import json
import requests
URL = 'http://api.bcb.gov.br/dados/serie/bcdata.sgs.4447/dados?formato=json'
dados = requests.get(URL)
#vamos usar a biblioteca json para ler os dados
listaDados = dados.json()
dataframe = pd.DataFrame(listaDados)
datainicial = str(dataframe.head(1).iat[0, 0])
datafinal = str(dataframe.tail(1).iat[0 , 0])
nomeArquivo = 'ipca(' + datainicial + '_a_' + datafinal + ').csv'
dataframe.to_csv('ipca.csv')