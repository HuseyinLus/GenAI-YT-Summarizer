from fastapi import FastAPI
from api.routes import summary_routes

app = FastAPI(title="Youtube video summariser api")
app.include_router(summary_routes.router, prefix="/api")

