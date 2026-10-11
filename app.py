import os
import socket
from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import redis

app = FastAPI()
cache = redis.Redis(host=os.getenv("REDIS_HOST", "db-service"), port=6379)

@app.get("/", response_class=PlainTextResponse)
def index():
    hits = cache.incr("hits")
    return f"Bonjour ! Cette page a été vue {hits} fois. Je suis le conteneur {socket.gethostname()}\n"
