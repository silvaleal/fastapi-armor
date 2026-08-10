from core.queue import Queue
from dotenv import load_dotenv

import asyncio

load_dotenv()

queue = Queue()

print("""
REVISOPASS - QUEUE
Rodando
      """)

# for _ in range(1):
#     queue.insert("send-email", {'user': 'johnDoe'})

try:
    asyncio.run(queue.run())
except KeyboardInterrupt:
    queue.running = False
