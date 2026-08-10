from database import Database

import json
import asyncio

# Handlers
# from .handlers.<name> import *

class Queue:
    def __init__(self):
        self.running = True

    def insert(self, item, data:dict):
        Database().commit(f"INSERT INTO queue (field, data) VALUES (%s, %s)", (item, json.dumps(data)))

    def get(self):
        item = Database().first("SELECT * FROM queue WHERE status = 0 LIMIT 1")
        return item if item else None

    def dispatch(self, field:str, data:dict):
        handlers = {
            # "key-handler": FunctionHandler(data)
        }
        
        return handlers[field] if field in handlers else None

    async def run(self):
        while self.running:
            item = self.get()

            if not item: continue

            print(f'QUEUE RUNNING #{item[0]}')

            handler = self.dispatch(item[1], json.loads(item[2]))
            
            if handler:
                handler.run()
                Database().commit(f"UPDATE queue SET status = 1 WHERE id = '{item[0]}'")
            else:
                print(handler)

            await asyncio.sleep(1)
