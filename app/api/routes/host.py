from fastapi import APIRouter
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
import logging
import json

from app.api.interface.host import schemas, interface

_logger = logging.getLogger('app')
router = APIRouter()
_host = interface.HostInterface()

@router.get('/get_multi')
async def get_multi():
  res = _host.get_multi()
  a = {
    'data': json.loads(res.to_json())
  }
  _logger.info(a['data'])
  return JSONResponse(content=jsonable_encoder(a))

@router.get('/get/{host_id}')
async def get(host_id: str):
  res = _host.get(host_id)
  _logger.info(res.to_json())
  return res.to_json()

@router.post('/create')
async def create(data: schemas.HostCreate):
  res = _host.create(data)
  _logger.info(res.to_json())
  return res.to_json()

@router.put('/update/{host_id}')
async def update(host_id: str, data: schemas.HostUpdate):
  res = _host.update(host_id, data)
  _logger.info(res.to_json())
  return res.to_json()

@router.delete('/delete/{host_id}')
async def delete(host_id: str):
  res = _host.delete(host_id)
  """ _logger.info(res.to_json()) """
  return {}