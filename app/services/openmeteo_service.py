import requests

def buscar_coordenadas(nome_cidade):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": nome_cidade,
        "count": 1,
        "language": "pt",
        "format": "json"
    }

    resposta = requests.get(url, params=params, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    resultados = dados.get("results", [])

    if not resultados:
        return None

    local = resultados[0]

    return {
        "cidade": local["name"],
        "estado": local.get("admin1"),
        "pais": local.get("country"),
        "latitude": local["latitude"],
        "longitude": local["longitude"],
        "timezone": local.get("timezone")
    }


def buscar_clima_openmeteo(latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": ",".join([
            "temperature_2m",
            "relative_humidity_2m",
            "apparent_temperature",
            "weather_code",
            "wind_speed_10m",
            "wind_gusts_10m"
        ]),
        "daily": ",".join([
            "weather_code",
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_probability_max",
            "uv_index_max"
        ]),
        "forecast_days": 7,
        "timezone": "auto"
    }

    resposta = requests.get(url, params=params, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()
    atual = dados["current"]

    diario = dados ["daily"]

    previsao = []

    for i in range(len(diario["time"])):
            previsao.append({
            "data": diario["time"][i],
            "codigo_clima": diario["weather_code"][i],
            "temperatura_maxima": diario["temperature_2m_max"][i],
            "temperatura_minima": diario["temperature_2m_min"][i],
            "probabilidade_chuva": diario["precipitation_probability_max"][i],
            "indice_uv": diario["uv_index_max"][i]
        })

    return {
        "temperatura": atual["temperature_2m"],
        "umidade": atual["relative_humidity_2m"],
        "sensacao_termica": atual["apparent_temperature"],
        "codigo_clima": atual["weather_code"],
        "vento": atual["wind_speed_10m"],
        "rajadas": atual["wind_gusts_10m"],
        "previsao_diaria": previsao,
        "indice_uv": diario["uv_index_max"][0]
    }




resultado = buscar_coordenadas("Rio de Janeiro")

if resultado:
    clima = buscar_clima_openmeteo(
        resultado["latitude"],
        resultado["longitude"]
    )
    print(resultado)
    print(clima)
else:
    print("Cidade não encontrada.")