from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    return {"message": f"Hello from FastAPI - {hostname}"}

@app.get("/health")
def health_check():
    return {"status": "ok"}