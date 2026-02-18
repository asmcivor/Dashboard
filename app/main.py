from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )

@app.get("/menu", response_class=HTMLResponse)
def mobile_menu(request: Request):
    return templates.TemplateResponse(
        "partials/menu.html",
        {"request": request}
    )

@app.get("/menu-close", response_class=HTMLResponse)
def mobile_menu_close(request: Request):
    return HTMLResponse("")

@app.get("/time", response_class=HTMLResponse)
def get_time(request: Request):
    return templates.TemplateResponse(
        "partials/time.html",
        {"request": request, "time": datetime.now().strftime("%H:%M:%S")}
    )