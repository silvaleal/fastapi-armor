from database import Database

from core.notifications.discord import RateLimitNotifier

from core.rate_limit import RateLimit

class Controller:
    def __init__(self, request, response):
        self.request = request
        self.http_response = response

    def _authorization(self, token:str):
        if not token:
            raise Exception("Autorização não encontrada.")

        partial_token = token.split(' ')

        if (len(partial_token) < 2):
            raise Exception("Autorização inválida.")

        auth_type = partial_token[0]
        auth_token = partial_token[1]

        if auth_type != 'Bearer':
            raise Exception("Autorização inválida.")

        if not auth_token:
            raise Exception("Autorização não encontrada.")

        user = Database().first("SELECT * FROM users WHERE api_token = %s", (auth_token,))

        if not user:
            raise Exception("Autorização inválida.")

        return user

    def _rate_limit(self, data:dict):
        if not RateLimit(data['api_token']).handler():
            RateLimitNotifier().send(data)

            raise Exception("Taxa de solicitações excedida.")
            # return self.send({
            #     "message": "Taxa de solicitações excedida."
            # }, 429)

    def send(self, data, status_code:int = 200):
        self.http_response.status_code = status_code
        return data
