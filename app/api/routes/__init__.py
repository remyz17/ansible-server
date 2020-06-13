from fastapi import APIRouter
from app.api.routes import host, group

api_router = APIRouter()
api_router.include_router(host.router, prefix='/host')
api_router.include_router(group.router, prefix='/group')