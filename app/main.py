from fastapi import FastAPI
from app.routes.clima import router
from pathlib import Path
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent.parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

@app.get("/", include_in_schema=False)
def pagina_inicial():
    return FileResponse(BASE_DIR / "static" / "index.html")

app.include_router(router)

@app.get("/")
def inicio():
    return{
        "status": "ok",
        "mensagem": "FastAPI Funcionando!"

    }


