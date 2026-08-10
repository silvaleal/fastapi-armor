from database import Database

class RateLimit:
    def __init__(self, api_token:str):
        self.api_token = api_token
        self.limit = 5
        self.interval = 2 # minutos

    def count(self):
        result = Database().first(f"SELECT COUNT(*) FROM api_requests WHERE api_token = %s AND created_at >= NOW() - INTERVAL %s MINUTE", (self.api_token, self.interval, ))
        return result[0] if result else 0

    def check(self):
        if self.count() >= self.limit:
            return False
        return True

    def register(self):
        Database().commit("INSERT INTO api_requests (api_token) VALUES (%s)", (self.api_token,))

    def handler(self):
        if not self.check():
            return False
        
        self.register()
        return True
