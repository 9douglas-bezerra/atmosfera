
from app.services.recomendacao_service import recomendar_praticar_esportes

previsao = {
    "temperatura_max": 23,
    "probabilidade_chuva": 10,
    "umidade": 55,
    "vento": 12,
    "indice_uv": 2
}

qualidade_ar = {
    "qualidade": "Boa"
}

resultado = recomendar_praticar_esportes(
    previsao,
    qualidade_ar
)

print(resultado)
