'''@email [brunosilvamardonado@gmail.com]
## @create date 2022-05-17 21:09:29
## @modify date 2022-05-17 21:09:29
## @desc [Scrapper Python 3.10 ]
##@author [Bruno Martins]
'''

import requests

#link para bscar dado usado na API

url = 'http://economia.awesomeapi.com.br/all/USD-BRL'
url2 = 'http://economia.awesomeapi.com.br/all/BRL-USD'
url3 = 'https://economia.awesomeapi.com.br/all/EUR-BRL'
url4 = 'https://economia.awesomeapi.com.br/all/BRL-EUR'
url5 = 'https://economia.awesomeapi.com.br/all/BTC-BRL'

# Busca dados na API

response = requests.get(url)
response2 = requests.get(url2)
response3 = requests.get(url3)
response4 = requests.get(url4)
response5 = requests.get(url5)

# Verifica se os dados funcionaram

if response.status_code and response2.status_code and response3.status_code  and response4.status_code and response5.status_code == 200:
    dolar_value = response.json()['USD']['low']
    dolar_value2 = response2.json()['BRL']['low']
    euro_value3 = response3.json()['EUR']['low']
    euro_value4 = response4.json()['BRL']['low']
    bit_value5 = response5.json()['BTC']['low']
    print(f'O valor do Dólar atualemten é R${dolar_value}.')
    print(f'O valor do Real está em U${dolar_value2}.') 
    print(f'O valor do Euro atualmente é R${euro_value3}.')
    print(f'O valor do Real em EUR é R${euro_value4}')
    print(f'O valor do BTC em Reais é R${bit_value5} mil')
else:
    print('A busca de valor na API publica falhou!')