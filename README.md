
# ☀️ Atmosfera

### Aplicação meteorológica com recomendações personalizadas

O Atmosfera é uma aplicação web desenvolvida para transformar
dados meteorológicos em informações úteis para o dia a dia.

Além de consultar a previsão do tempo, o sistema oferece
recomendações personalizadas de acordo com a atividade
que o usuário deseja realizar.

## 🚀 Funcionalidades

- Consulta meteorológica por cidade
- Temperatura atual e sensação térmica
- Umidade e velocidade do vento
- Previsão meteorológica para 7 dias
- Probabilidade de chuva
- Qualidade do ar (PM2.5 e PM10)
- Recomendações personalizadas para:
  - Ir à praia
  - Lavar roupas
  - Praticar esportes
  - Sair para trabalhar
- Interface web responsiva
- Ícones representando as condições meteorológicas

## 🛠️ Tecnologias utilizadas

### Backend
- Python
- FastAPI
- APIs REST
- Open-Meteo
- Uvicorn
- Requests

### Frontend
- HTML5
- CSS3
- JavaScript
- Lucide Icons

### Ferramentas
- Visual Studio Code
- Git
- GitHub

## ⚙️ Como executar o projeto

Clone o repositório:

```bash
git clone https://github.com/9douglas-bezerra/atmosfera.git
```

Entre na pasta:

```bash
cd atmosfera
```

Crie um ambiente virtual:

```bash
python -m venv venv
```

Ative o ambiente virtual no Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o servidor:

```bash
uvicorn app.main:app --reload
```

Acesse no navegador:

http://127.0.0.1:8000

Documentação da API:

http://127.0.0.1:8000/docs

## 🌐 API utilizada

O projeto utiliza a Open-Meteo para obter dados
meteorológicos e informações sobre qualidade do ar.

https://open-meteo.com/

## 📌 Melhorias futuras

- Localização automática por GPS
- Histórico de consultas
- Alertas meteorológicos
- Melhorias na experiência do usuário
- Integração com aplicativo mobile

## 👨‍💻 Autor

Douglas Bezerra

Estudante de Análise e Desenvolvimento de Sistemas,
com foco em desenvolvimento Back-end.

GitHub: https://github.com/9douglas-bezerra
