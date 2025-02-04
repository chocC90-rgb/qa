from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Montar los archivos estáticos correctamente
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar Jinja2Templates con el directorio correcto de templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    # Renderizar el template 'index.html' con el contexto necesario
    return templates.TemplateResponse(
        "login.html", {"request": request}
    )

@app.get("/registro", response_class=HTMLResponse)
async def read_item(request: Request):
    # Renderizar el template 'index.html' con el contexto necesario
    return templates.TemplateResponse(
        "registro.html", {"request": request}
    )