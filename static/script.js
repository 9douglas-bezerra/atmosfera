
const formulario = document.getElementById("form-clima");

// Descrições meteorológicas
const descricoesClima = {
    0: "Céu limpo",
    1: "Predominantemente limpo",
    2: "Parcialmente nublado",
    3: "Nublado",
    45: "Nevoeiro",
    48: "Nevoeiro com geada",
    51: "Garoa fraca",
    53: "Garoa moderada",
    55: "Garoa intensa",
    56: "Garoa congelante fraca",
    57: "Garoa congelante intensa",
    61: "Chuva fraca",
    63: "Chuva moderada",
    65: "Chuva forte",
    66: "Chuva congelante fraca",
    67: "Chuva congelante forte",
    71: "Neve fraca",
    73: "Neve moderada",
    75: "Neve forte",
    77: "Grãos de neve",
    80: "Pancadas de chuva fracas",
    81: "Pancadas de chuva moderadas",
    82: "Pancadas de chuva fortes",
    85: "Pancadas de neve fracas",
    86: "Pancadas de neve fortes",
    95: "Trovoadas",
    96: "Trovoadas com granizo fraco",
    99: "Trovoadas com granizo forte"
};

// Formata a data para o padrão brasileiro
function formatarData(dataISO) {

    const [ano, mes, dia] = dataISO.split("-").map(Number);

    const data = new Date(ano, mes - 1, dia);

    const diaSemana = new Intl.DateTimeFormat("pt-BR", {
        weekday: "short"
    }).format(data);

    return `${diaSemana} ${String(dia).padStart(2, "0")}/${String(mes).padStart(2, "0")}`;
}

// Escolhe o ícone conforme o código meteorológico
function obterIconeClima(codigo) {

    if (codigo === 0 || codigo === 1) {
        return "sun";
    }

    if (codigo === 2) {
        return "cloud-sun";
    }

    if (codigo === 3) {
        return "cloud";
    }

    if ([45, 48].includes(codigo)) {
        return "cloud-fog";
    }

    if ([51, 53, 55, 56, 57].includes(codigo)) {
        return "cloud-drizzle";
    }

    if ([61, 63, 65, 66, 67, 80, 81, 82].includes(codigo)) {
        return "cloud-rain";
    }

    if ([71, 73, 75, 77, 85, 86].includes(codigo)) {
        return "cloud-snow";
    }

    if ([95, 96, 99].includes(codigo)) {
        return "cloud-lightning";
    }

    return "cloud";
}

// Evento de consulta do clima
formulario.addEventListener("submit", async function(evento) {

    // Impede que a página recarregue
    evento.preventDefault();

    // Captura os dados informados pelo usuário
    const cidade = document.getElementById("cidade").value;
    const perfil = document.getElementById("perfil").value;

    const mensagem = document.getElementById("mensagem");
    const resultado = document.getElementById("resultado");

    mensagem.textContent = "Consultando o clima...";
    resultado.hidden = true;

    try {

        // Monta os parâmetros da consulta
        const parametros = new URLSearchParams({
            cidade: cidade,
            perfil: perfil
        });

        // Faz a requisição ao FastAPI
        const resposta = await fetch(`/clima?${parametros}`);

        if (!resposta.ok) {
            throw new Error("Não foi possível consultar o clima.");
        }

        // Converte a resposta JSON em objeto JavaScript
        const dados = await resposta.json();

        // Exibe as informações meteorológicas
        document.getElementById("local").textContent =
            `${dados.cidade} - ${dados.estado}`;

        document.getElementById("temperatura").textContent =
            `${dados.temperatura} °C`;

        // Descrição do clima atual
        document.getElementById("descricao").textContent =
            descricoesClima[dados.codigo_clima] || "Condição não informada";

        document.getElementById("sensacao").textContent =
            `Sensação térmica: ${dados.sensacao_termica} °C`;

        document.getElementById("umidade").textContent =
            `Umidade: ${dados.umidade}%`;

        document.getElementById("vento").textContent =
            `Vento: ${dados.vento} km/h`;

        document.getElementById("qualidade").textContent =
            `Qualidade do ar: ${dados.qualidade_ar.qualidade}`;

        // Exibe a recomendação personalizada
        const recomendacao = dados.recomendacao_perfil;

        document.getElementById("recomendacao").textContent =
            typeof recomendacao === "string"
                ? recomendacao
                : recomendacao == null
                    ? "Recomendação indisponível."
                    : JSON.stringify(recomendacao);

        // Exibe a previsão dos próximos dias
        const previsao = document.getElementById("previsao");

        previsao.innerHTML = "";

        dados.previsao_diaria.forEach(function(dia) {

            // Cria o cartão
            const card = document.createElement("div");
            card.className = "dia";

            // Data formatada
            const data = document.createElement("h4");
            data.textContent = formatarData(dia.data);

            // Ícone meteorológico
            const icone = document.createElement("i");
            const nomeIcone = obterIconeClima(dia.codigo_clima);

            icone.setAttribute("data-lucide", nomeIcone);
            icone.className = "icone-clima";

            // Temperaturas mínima e máxima
            const temperatura = document.createElement("p");

            temperatura.textContent =
                `${dia.temperatura_minima}° / ${dia.temperatura_maxima}°`;

            // Probabilidade de chuva
            const chuva = document.createElement("p");
            chuva.className = "chuva";

            chuva.textContent =
                `💧 ${dia.probabilidade_chuva}% de chuva`;

            // Adiciona os elementos ao cartão
            card.append(data, icone, temperatura, chuva);

            // Adiciona o cartão à página
            previsao.appendChild(card);

        });

        // Converte os elementos em ícones SVG
        if (typeof lucide !== "undefined") {
            lucide.createIcons();
        } else {
            console.warn("Biblioteca de ícones Lucide não carregada.");
        }

        // Mostra o resultado
        mensagem.textContent = "";
        resultado.hidden = false;

    } catch (erro) {

        // Registra possíveis erros no Console
        console.error("Erro ao consultar clima:", erro);

        mensagem.textContent = erro.message;

    }

});
