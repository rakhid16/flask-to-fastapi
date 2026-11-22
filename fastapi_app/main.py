from pathlib import Path

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from joblib import load

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "modeling" / "simple_model.pkl"

app = FastAPI()
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

model = load(MODEL_PATH)
templates = Jinja2Templates(directory=BASE_DIR / "templates")


@app.get("/html_css_js/", response_class=HTMLResponse)
def page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "data": "ini dari FASTAPI"},
    )


@app.post("/ml_serving")
def ml_serving(sentence: str):
    return {"Hasilnya adalah": model.classify(sentence)}


@app.get("/{sentence}")
def index(sentence: str):
    return {"hello": sentence}
