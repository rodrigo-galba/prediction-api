import os
import uvicorn

from fastapi import FastAPI
from pydantic import BaseModel
from mangum import Mangum

STAGE = os.environ.get('STAGE', None)
openapi_prefix = "/" if not STAGE else f'/{STAGE}'

app = FastAPI(title="MyAwesomeApp", root_path=openapi_prefix)

# Mangum Handler, this is so important
handler = Mangum(app)


@app.get("/")
def index():
    return {"message": "Prediction API"}

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
