from core.api import Router

from fastapi import Request, Response
from v1.controllers.home import HomeController

router = Router(prefix="v1") # Sem barra

def home(request: Request, response: Response):
    return HomeController(request, response).index()

router.get("/", home)