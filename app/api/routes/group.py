from fastapi import APIRouter
import logging

from app.api.interface.group import schemas, interface
from app.api.interface.host.interface import HostInterface

_logger = logging.getLogger('app')
router = APIRouter()
_group = interface.GroupInterface()
_host = HostInterface()

@router.get('/get_multi')
async def get_multi():
  res = _group.get_multi()
  _logger.info(res.to_json())
  return res.to_json()

@router.get('/get/{group_id}')
async def get(group_id: str):
  res = _group.get(group_id)
  _logger.info(res.to_json())
  return res.to_json()

@router.post('/create')
async def create(data: schemas.GroupCreate):
  res = _group.create(data)
  _logger.info(res.to_json())
  return res.to_json()

@router.put('/update/{group_id}')
async def update(group_id: str, data: schemas.GroupUpdate):
  res = _group.update(group_id, data)
  _logger.info(res.to_json())
  return res.to_json()

@router.delete('/delete/{group_id}')
async def delete(group_id: str):
  res = _group.delete(group_id)
  return {}