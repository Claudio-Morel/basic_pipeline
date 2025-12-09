from fastapi import FastAPI
from lib import suma

app = FastAPI()

@app.get("/")
def root():
    return {"mensaje": "el despliegue fue exitoso"}

@app.get("/suma/{a}/{b}")
def calcular(a: int, b: int):
    return {"resultado": suma(a, b)}
