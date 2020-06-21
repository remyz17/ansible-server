import logging
from fastapi import APIRouter

from app.api.serializers import host_serialize
from app.models.host import Host
from app.models.group import Group

_logger = logging.getLogger('app')
router = APIRouter()

@router.get('/get_multi')
async def get_multi():
  cursor = Host.find()
  hosts = [host.dump() for host in await cursor.to_list(length=80)]
  _logger.info(hosts)
  return hosts

@router.get('/get/{host_id}')
async def get(host_id: str):
  host = await Host.get(host_id)
  _logger.info(host.dump())
  return host.dump()

@router.post('/create')
async def create(data: host_serialize.HostCreate):
  host = Host(hostname=data.hostname)
  await host.commit()
  return host.dump()

@router.put('/update/{host_id}')
async def update(host_id: str, data: host_serialize.HostUpdate):
  host = await Host.get(host_id)
  host = await host.update(data)
  _logger.info(host.dump())
  return host.dump()

@router.delete('/delete/{host_id}')
async def delete(host_id: str):
  host = await Host.get(host_id).remove()
  return {}