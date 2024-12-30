import requests
from dotenv import load_dotenv
import os

load_dotenv()

def extract_temp_data(lat, lon, lang, units, apikey):
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}&lang={lang}&units={units}"

    response = requests.get(url)
    data = response.json()

    return data

def tranform_temp_data(data):
    clima = data['weather'][0]['main']
    clima_detail = data['weather'][0]['description']
    temp = data['main']['temp']
    sensacao_termica = data['main']['feels_like']
    temp_min = data['main']['temp_min']
    temp_max = data['main']['temp_max']
    pressao_atm = data['main']['pressure']
    umidade = data['main']['humidity']
    visibilidade = data['visibility']
    velocidade_vento = data['wind']['speed']
    direcao_vento = data['wind']['deg']
    cidade = data['name']

    dados_transformados = {
        "clima": clima,
        "clima_detail": clima_detail,
        "temp": temp,
        "sensacao_termica": sensacao_termica,
        "temp_min": temp_min,
        "temp_max": temp_max,
        "pressao_atm": pressao_atm,
        "umidade": umidade,
        "visibilidade": visibilidade,
        "velocidade_vento": velocidade_vento,
        "direcao_vento": direcao_vento,
        "cidade": cidade,
    }

    return dados_transformados

if __name__== "__main__":
    APIKEY = os.getenv("APIKEY")

    lat = -5.917550296148145
    lon = -35.20936332816193
    lang = "pt_br"
    units = "metric"

    data = extract_temp_data(lat, lon, lang, units, apikey=APIKEY)
    new_data = tranform_temp_data(data)

    print(new_data)