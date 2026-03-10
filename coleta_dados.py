import requests

url="https://api.portaldatransparencia.gov.br/api-de-dados/licitacoes"

headers={"accept":"application/json"}

try:
 r=requests.get(url,headers=headers)
 dados=r.json()

 print("SOC Transparencia ativo")

 print(type(dados))
 print(dados)

except Exception as e:
 print("erro:",e)

