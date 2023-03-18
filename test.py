import requests

url = "https://www.ine.pt/ine/json_indicador/pindica.jsp?op=2&varcd=0008073&lang=PT"

response = requests.get(url)

data = response.json()

print(data)