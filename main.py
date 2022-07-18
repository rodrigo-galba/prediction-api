import os
import uvicorn

from fastapi import FastAPI, Form
from pydantic import BaseModel
from mangum import Mangum

STAGE = os.environ.get('STAGE', None)
openapi_prefix = "/" if not STAGE else f'/{STAGE}'

app = FastAPI(title="MyAwesomeApp", root_path=openapi_prefix)

# Mangum Handler, this is so important
handler = Mangum(app)

class PredictModel(BaseModel):
    message: str

@app.get("/")
def index():
    return {"message": "Prediction API"}

@app.post("/predict")
async def predict(model: PredictModel):
    prediction = predict_completions(model.message)
    return { "message": prediction }

def predict_completions(message: str):
    # Load model file
    # Load unique words
    # Call predict function
    # lib/predict.py
    # TODO roda as tretas do KERAS
    return message


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
