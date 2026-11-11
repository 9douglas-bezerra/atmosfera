import requests


def calcular_media(valores):
    valores_validos = [
        valor for valor in valores
        if valor is not None
    ]

    if not valores_validos:
        return None

    return sum(valores_validos) / len(valores_validos)


def buscar_qualidade_ar(latitude, longitude):

    url = "https://air-quality-api.open-meteo.com/v1/air-quality"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": "pm2_5,pm10",
        "past_hours": 24,
        "forecast_hours": 1,
        "timezone": "auto"
    }

    try:
        resposta = requests.get(
            url,
            params=params,
            timeout=10
        )

        print("STATUS:", resposta.status_code)

        dados = resposta.json()

        print("DADOS DA QUALIDADE DO AR:")
        print(dados)

        resposta.raise_for_status()

        horario = dados["hourly"]

        pm2_5 = calcular_media(
            horario["pm2_5"][-24:]
        )

        pm10 = calcular_media(
            horario["pm10"][-24:]
        )

        print("PM2.5:", pm2_5)
        print("PM10:", pm10)

        if pm2_5 is None or pm10 is None:
            return {
                "qualidade": "Indisponível",
                "pm2_5": None,
                "pm10": None
            }

        if pm2_5 <= 15 and pm10 <= 45:
            qualidade = "Boa"

        elif pm2_5 <= 25 and pm10 <= 60:
            qualidade = "Moderada"

        else:
            qualidade = "Ruim"

        return {
            "qualidade": qualidade,
            "pm2_5": round(pm2_5, 1),
            "pm10": round(pm10, 1)
        }

    except Exception as erro:

        print("ERRO NA QUALIDADE DO AR:")
        print(erro)

        return {
            "qualidade": "Indisponível",
            "pm2_5": None,
            "pm10": None
        }