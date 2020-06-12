from fastapi import APIRouter
from app.api.routes import hosts

api_router = APIRouter()
api_router.include_router(hosts.router, prefix='/host')