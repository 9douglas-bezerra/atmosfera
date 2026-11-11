
from fastapi import APIRouter, HTTPException
from app.services.openmeteo_service import (buscar_coordenadas, buscar_clima_openmeteo)
from app.services.qualidade_ar_service import buscar_qualidade_ar
from app.services.recomendacao_service import (
    recomendar_ir_a_praia, 
    recomendar_lavar_roupa, 
    recomendar_praticar_esportes,
    recomendar_ir_trabalhar
    )


router = APIRouter()

@router.get("/clima")
def buscar_clima(cidade: str, perfil: str | None = None):

    coordenadas = buscar_coordenadas(cidade)
    if coordenadas is None: 
        raise HTTPException(status_code=404, detail="Erro: cidade não encontrada")

    clima = buscar_clima_openmeteo(
        coordenadas["latitude"],
        coordenadas["longitude"]
    )

    qualidade_ar = buscar_qualidade_ar(
        coordenadas["latitude"],
        coordenadas["longitude"]
    )

    # Dados que recomendação irá usar
    previsao_diaria=clima["previsao_diaria"]
    hoje = previsao_diaria[0]


    previsao_perfil = {
        "temperatura": clima.get("temperatura"),
        "temperatura_max": hoje.get("temperatura_maxima"),
        "probabilidade_chuva": hoje.get("probabilidade_chuva"),
        "precipitacao_probabilidade": hoje.get("probabilidade_chuva"),
        "umidade": clima.get("umidade"),
        "vento": clima.get("vento"),
        "indice_uv": hoje.get("indice_uv")
    }
    
    # Dados que recomendação irá usar de qualidade do ar
    dados_qualidade_ar = qualidade_ar.get("qualidade", qualidade_ar)

    qualidade_ar_perfil = {
        "qualidade": qualidade_ar.get("qualidade")
        }


    # Recomendação de acordo com o perfil
    recomendacao_perfil = None

    if perfil == "praia":
        recomendacao_perfil = recomendar_ir_a_praia(previsao_perfil, qualidade_ar_perfil)
    
    elif perfil == "lavar_roupa":
        recomendacao_perfil = recomendar_lavar_roupa(previsao_perfil, qualidade_ar_perfil)

    elif perfil == "esportes":
        recomendacao_perfil = recomendar_praticar_esportes(previsao_perfil, qualidade_ar_perfil)

    elif perfil == "trabalho":
         recomendacao_perfil = recomendar_ir_trabalhar(previsao_perfil, qualidade_ar_perfil)

    return {
        "cidade": coordenadas["cidade"],
        "estado": coordenadas["estado"],
        "pais": coordenadas["pais"],
        "latitude": coordenadas["latitude"],
        "longitude": coordenadas["longitude"],
        "timezone": coordenadas["timezone"],

        "temperatura": clima["temperatura"],
        "umidade": clima["umidade"],
        "sensacao_termica": clima["sensacao_termica"],
        "codigo_clima": clima["codigo_clima"],
        "vento": clima["vento"],
        "rajadas": clima["rajadas"],

        "qualidade_ar": qualidade_ar,
        "previsao_diaria": clima["previsao_diaria"],

        "perfil": perfil,
        "recomendacao_perfil": recomendacao_perfil
    }
