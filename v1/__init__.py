from core.api import Version, Router

from fastapi import FastAPI

class V1(Version):
    def __init__(self, app:FastAPI, router:Router):
        super().__init__(app, router)