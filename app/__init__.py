from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import logging

from app.core import config

app = FastAPI(
  title=config.NAME
)

class SPAStaticFiles(StaticFiles):
    async def get_response(self, path, scope):
        response = await super().get_response(path, scope)
        if response.status_code == 404:
            response = await super().get_response('.', scope)
        return response

app.mount("/web/app/", StaticFiles(directory="%s/static" % __name__, html=True))

_logger = logging.getLogger('app')

if config.CORS_ORIGIN:
  app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in config.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

async def redirectSPA():
  response = RedirectResponse(url='/web/app/')
  return response

@app.get("/")
async def root():
    return await redirectSPA()