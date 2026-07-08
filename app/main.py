from fastapi import FastAPI

app = FastAPI(
    title="AI Business Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to AI Business Intelligence Platform"
    }