import logging

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware

from app.core import config
from app.db import database
from app.api.routes import api_router

_logger = logging.getLogger(__name__)

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


@app.on_event('startup')
async def event_startup():
  _logger.info('Ensuring model indexes created into database ...')
  from app.models import ensure_indexes
  await ensure_indexes()
  _logger.info('Model indexes created')

@app.on_event('shutdown')
async def event_shutdown():
  _logger.info('Closing connection to database ...')
  database.client.close()
  _logger.info('Connection closed')
  

app.include_router(api_router, prefix='/api')
app.mount('/_assets/', StaticFiles(directory='app/static/_assets'))
app.route('/', redirectSPA)