from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"service": "ml-observability-dashboard"}

@app.get("/metrics")
def metrics():
    return {
        "latency_ms": random.randint(20, 120),
        "cpu_usage": random.randint(40, 90),
        "memory_usage": random.randint(30, 85),
        "status": "healthy"
    }
