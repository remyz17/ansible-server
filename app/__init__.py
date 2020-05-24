from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import logging

from app.core import config

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
  return FileResponse('%s/static/index.html' % __name__)

@app.middleware("http")
async def add_custom_header(request, call_next):
    response = await call_next(request)
    if response.status_code == 404:
        return FileResponse('%s/static/index.html' % __name__)
    return response

@app.exception_handler(404)
def not_found(request, exc):
    return FileResponse('%s/static/index.html' % __name__)

app.mount('/_assets/', StaticFiles(directory='%s/static/_assets' % __name__))
app.route('/', redirectSPA)