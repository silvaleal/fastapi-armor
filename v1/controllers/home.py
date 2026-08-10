from fastapi import Request, Response
from ..controllers import Controller

class HomeController(Controller):
    def __init__(self, request:Request, response:Response):
        super().__init__(request, response)
        
    def index(self):
        return self.send({
            "message": "API ativa.",
            "doc": "/doc",
            })