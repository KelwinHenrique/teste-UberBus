#disponivel em: https://codigosimples.net/2017/05/15/criando-uma-api-de-filmes-em-cartaz-usando-python-e-heroku/
#PARTE1
from flask import Flask, jsonify, request
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
import os

#PARTE2
app = Flask(__name__)

#PARTE3
@app.route('/api/v1/filmes', methods=['GET'])
def filmes():
  page = requests.get("http://cdfuberaba.auttran.com/ajax/fulltable.php?codlinha=100&city=UBEN&d=")
  #print(page)
  #print(page.status_code)
  #print(page.content)
  soup = BeautifulSoup(page.content, 'html.parser')
  print(soup.prettify())

  #TESTES
  #Pegando o sentido do Onibus e ultima atualização
  temporeal = {}
  todos = []
  for nome in soup.find_all("td", class_="tidtd1"):
      temporeal[nome.text] = []
      todos.append(nome.text)
      print(temporeal)

  #Pegando os pontos e os horários
  tabelas = []
  for coluna in soup.find_all("td", class_="tidtd2"):
      tabela = []
      for linha in coluna.find_all("tr", class_="inttr1"):
          horario_previsto = linha.find("td", class_="inttd1_0").text
          ponto = linha.find("td", class_="inttd1_2").text
          dici = [horario_previsto, ponto]
          tabela.append(dici)
      tabelas.append(tabela)
  print(tabelas)
  return jsonify({'filmes': tabelas})

#PARTE4
if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='127.0.0.1', port=port)
