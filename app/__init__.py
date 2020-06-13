from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import logging

from app.core import config
from app.api.env import Env
from app.api.routes import api_router

_env = Env(production=False)

app = FastAPI(
  title=config.NAME
)

if config.CORS_ORIGIN:
  app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in config.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

async def redirectSPA():
  return FileResponse('app/static/index.html')

@app.middleware("http")
async def add_custom_header(request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        return await redirectSPA
    return response

@app.exception_handler(404)
async def not_found(request, exc):
    return await redirectSPA()

app.mount('/_assets/', StaticFiles(directory='app/static/_assets'))
app.route('/', redirectSPA)
app.include_router(api_router, prefix='/api')