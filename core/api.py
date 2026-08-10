from fastapi import FastAPI

class Version:
    def __init__(self, app:FastAPI, router:Router):
        self.router = router
        self.app = app
    
    def start(self):
        routes = self.router.routes
        
        for route in routes:
            print(f"ROUTE: {route} added")
            
            self.app.add_api_route(
                path=route,
                methods=[routes[route]['method']],
                endpoint=routes[route]['instance']
            )        

class Router:
    def __init__(self, prefix):
        self.routes = {}
        self.prefix = prefix
    
    def get(self, route:str, instance):
        self._create("GET", route, instance=instance)
        
    def post(self, route:str, instance):
        self._create("POST", route, instance=instance)
        
    def _create(self, method:str, route:str, instance):
        if route[0] == "/":
            route = route[1::]
            
        self.routes[f"/{self.prefix}/{route}"] = {
            "method": method,
            "instance": instance
        }
        