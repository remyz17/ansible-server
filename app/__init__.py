from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from starlette.middleware.cors import CORSMiddleware
import logging

from app.core import config

app = FastAPI(
  title=config.NAME
)

app.mount("/static", StaticFiles(directory="%s/static" % __name__), name="static")

_logger = logging.getLogger('app')

if config.CORS_ORIGIN:
  app.add_middleware(
    CORSMiddleware,
    allow_origins=[str(origin) for origin in config.CORS_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
  )

@app.get("/")
async def read_root():
    content = """
<!DOCTYPE html><html lang=en><head><meta charset=utf-8><meta http-equiv=X-UA-Compatible content="IE=edge"><meta name=viewport content="width=device-width,initial-scale=1"><link rel=icon href=/static/favicon.ico><title>test-vue</title><link href=/static/js/about.0f76db23.js rel=prefetch><link href=/static/css/app.3e7d65e5.css rel=preload as=style><link href=/static/js/app.f4773e42.js rel=preload as=script><link href=/static/js/chunk-vendors.6697755a.js rel=preload as=script><link href=/static/css/app.3e7d65e5.css rel=stylesheet></head><body><noscript><strong>We're sorry but test-vue doesn't work properly without JavaScript enabled. Please enable it to continue.</strong></noscript><div id=app></div><script src=/static/js/chunk-vendors.6697755a.js></script><script src=/static/js/app.f4773e42.js></script></body></html>
    """
    return HTMLResponse(content=content)

@app.get("/test")
async def getTest():
    return {"Hello": "test"}