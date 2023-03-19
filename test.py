import requests

url = "https://dados.gov.pt/s/dadosGovFiles/Crimesregistados20141993portipo.json"

response = requests.get(url)

data = response.json()

print(data)