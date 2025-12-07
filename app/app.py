from fastapi import FastAPI
from lib import suma

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "API funcionando"}

@app.get("/suma/{a}/{b}")
def calcular(a: int, b: int):
    return {"resultado": suma(a, b)}
