from fastapi import FastAPI
from dotenv import load_dotenv

from v1 import V1
from v1.routes import router as routerV1

load_dotenv()

app = FastAPI()

@app.on_event("startup")
async def startup():
    versions = [ # Suas versões da API
        V1(app, routerV1)
    ]

    for version in versions:
        version.start()