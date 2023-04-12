from fastapi import FastAPI
from src.service.PredictService import PredictService

app = FastAPI()
predictService = PredictService()


@app.get("/")
def hello():
    return {"response": "Hello world!!!"}


@app.post("/model")
def submit_to_model(observation: dict):
    return {"aprovado?": predictService.predict(observation)}