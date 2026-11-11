import requests


def recomendar_ir_a_praia(previsao, qualidade_ar):
    if previsao is None or qualidade_ar is None:
        return "Não é possível fornecer uma recomendação no momento."

    temperatura_max = previsao.get("temperatura_max")
    precipitacao_probabilidade = previsao.get("precipitacao_probabilidade")
    qualidade = qualidade_ar.get("qualidade")

    if temperatura_max is None or precipitacao_probabilidade is None or qualidade is None:
        return "Não é possível fornecer uma recomendação no momento."

    if (temperatura_max >= 25 and
            precipitacao_probabilidade < 20 and
            qualidade == "Boa"):
        return "É um bom dia para ir à praia!"
    else:
        return "Talvez não seja o melhor dia para ir à praia."


def recomendar_lavar_roupa(previsao, qualidade_ar):
    if previsao is None or qualidade_ar is None:
        return "Não é possível fornecer uma recomendação no momento."

    probabilidade_chuva = previsao.get("probabilidade_chuva")
    qualidade = qualidade_ar.get("qualidade")
    umidade = previsao.get("umidade")
    vento = previsao.get("vento")

    if (probabilidade_chuva is None
        or qualidade is None
        or umidade is None
        or vento is None):

        return "Não é possível fornecer uma recomendação no momento."

    if (probabilidade_chuva < 20
        and qualidade in ["Boa", "Moderada"]
        and 5 <= vento <= 30
        and umidade < 65
        ):

        return "É um bom dia para lavar roupa!"

    else:
        return "Talvez não seja o melhor dia para lavar roupa."


def recomendar_praticar_esportes(previsao, qualidade_ar):
    if previsao is None or qualidade_ar is None:
        return "Não é possível fornecer uma recomendação no momento."

    probabilidade_chuva = previsao.get("probabilidade_chuva")
    qualidade = qualidade_ar.get("qualidade")
    umidade = previsao.get("umidade")
    vento = previsao.get("vento")
    indice_uv = previsao.get("indice_uv")
    temperatura_max = previsao.get("temperatura_max")

    if (probabilidade_chuva is None
        or qualidade is None
        or umidade is None
        or vento is None
        or indice_uv is None):

        return "Não é possível fornecer uma recomendação no momento."
    

    # Condições de maior risco
    if (
        qualidade == "Ruim"
        or vento >= 40
        or (temperatura_max >= 27 and umidade >= 75)
    ):
        return (
            "Condições desfavoráveis para esportes ao ar livre. "
            "Prefira um ambiente protegido ou adie a atividade."
        )

    # Condições favoráveis
    elif (
        15 <= temperatura_max <= 25
        and 40 <= umidade <= 60
        and vento <= 20
        and probabilidade_chuva < 30
        and qualidade == "Boa"
        and indice_uv < 3
    ):
        return (
            "Ótimas condições para praticar esportes ao ar livre! "
            "Mantenha a hidratação durante a atividade."
        )

    # Condições que exigem atenção
    else:
        return (
            "É possível praticar atividades ao ar livre, "
            "mas as condições exigem atenção. "
            "Adapte a intensidade, mantenha a hidratação "
            "e evite horários de sol forte."
        )


def recomendar_ir_trabalhar(previsao, qualidade_ar):

    if previsao is None or qualidade_ar is None:
        return "Não é possível fornecer uma recomendação no momento."

    temperatura = previsao.get("temperatura")
    probabilidade_chuva = previsao.get("precipitacao_probabilidade")
    umidade = previsao.get("umidade")
    vento = previsao.get("vento")
    qualidade = qualidade_ar.get("categoria")

    if any(valor is None for valor in [
        temperatura,
        probabilidade_chuva,
        umidade,
        vento,
        qualidade
    ]):
        return "Não é possível fornecer uma recomendação no momento."

    recomendacoes = []

    if probabilidade_chuva >= 60:
        recomendacoes.append(
            "Alta possibilidade de chuva. Leve guarda-chuva "
            "e tenha cuidado no deslocamento."
        )
    elif probabilidade_chuva >= 30:
        recomendacoes.append(
            "Existe possibilidade de chuva. "
            "É aconselhável levar guarda-chuva."
        )

    if temperatura >= 32:
        recomendacoes.append(
            "O dia estará quente. Use roupas leves "
            "e mantenha a hidratação."
        )
    elif temperatura <= 15:
        recomendacoes.append(
            "A temperatura está baixa. "
            "Leve um agasalho."
        )

    if umidade >= 80 and temperatura >= 28:
        recomendacoes.append(
            "O calor e a umidade elevada podem "
            "aumentar o desconforto térmico."
        )
    elif umidade <= 30:
        recomendacoes.append(
            "A umidade está baixa. "
            "Mantenha a hidratação."
        )

    if vento >= 40:
        recomendacoes.append(
            "Atenção aos ventos fortes durante "
            "o deslocamento."
        )

    if qualidade == "Ruim":
        recomendacoes.append(
            "A qualidade do ar está ruim. "
            "Reduza a exposição prolongada ao ar livre."
        )

    if not recomendacoes:
        return (
            "As condições meteorológicas estão favoráveis "
            "para o deslocamento ao trabalho."
        )

    return " ".join(recomendacoes)



