from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


# ---------- Base Page ----------
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "base.html",
        {"request": request, "active": "dashboard"}
    )


# ---------- Menu Partial ----------
@app.get("/menu", response_class=HTMLResponse)
def menu(request: Request, active: str = "dashboard"):
    return templates.TemplateResponse(
        "partials/menu.html",
        {"request": request, "active": active}
    )


# ---------- Content Routes ----------
@app.get("/dashboard", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse(
        "partials/dashboard.html",
        {"request": request}
    )


@app.get("/reports", response_class=HTMLResponse)
def reports(request: Request):
    return templates.TemplateResponse(
        "partials/reports.html",
        {"request": request}
    )


@app.get("/settings", response_class=HTMLResponse)
def settings(request: Request):
    return templates.TemplateResponse(
        "partials/settings.html",
        {"request": request}
    )
