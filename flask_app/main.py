from pathlib import Path

from joblib import load
from flask import Flask, render_template

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR.parent / "modeling" / "simple_model.pkl"

app = Flask(__name__)
model = load(MODEL_PATH)


@app.get("/")
def index():
    return {"hello": "world"}


@app.get("/html_css_js/<sentence>")
def html_css_js(sentence):
    return render_template("index.html", data=sentence)


@app.get("/ml_serving/<sentence>")
def ml_serving(sentence):
    return model.classify(sentence)


if __name__ == "__main__":
    app.run(debug=True)
