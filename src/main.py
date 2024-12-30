import requests

url = "https://fakestoreapi.com/users/"

response = requests.get(url)
data = response.json()[0]

for dado in data:
    nome_completo = f"{
        ['name']['firstname']} {data['name']['lastname']}"
    email = data['email']
    telefone = data['phone']
    cidade = data["address"]["city"]
    rua = data["address"]["street"]
    numero = data["address"]["number"]
    cep = data["address"]["zipcode"]

    dados_transformados = {
        "nome_completo": nome_completo,
        "email": email,
        "telefone": telefone,
        "cidade": cidade,
        "rua": rua,
        "numero": numero,
        "cep": cep
    }

    print(dados_transformados)