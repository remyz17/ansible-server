import logging
from fastapi import APIRouter
from time import sleep

from app.api.serializers import host_serialize
from app.api.models.host import Host, HostVar
from app.api.models.group import Group

_logger = logging.getLogger('app')
router = APIRouter()

@router.get('/get_multi')
async def get_multi():
  cursor = Host.find()
  sleep(3)
  hosts = [host.dump() for host in await cursor.to_list(length=80)]
  _logger.info(hosts)
  return hosts

@router.get('/get/{host_id}')
async def get(host_id: str):
  host = await Host.get(host_id)
  """ group = await Group.get(host.group_id)
  _logger.info(group.dump()) """
  _logger.info(host.dump())
  sleep(3)
  return host.dump()

@router.post('/create')
async def create(data: host_serialize.HostCreate):
  host = Host(hostname=data.hostname, hostvars=[{'key': 'ahah', 'value': 'test val'}])
  if hasattr(data, 'group_id'):
    group = await Group.get(data.group_id)
    if group:
      host.group_id = group
  if hasattr(data, 'hostvars'):
    for var in data.hostvars:
      new_var = HostVar(key=var.key, value=var.value)
      await host.add_var(new_var)
  await host.commit()
  return host.dump()

@router.put('/update/{host_id}')
async def update(host_id: str, data: host_serialize.HostUpdate):
  host = await Host.get(host_id)
  host.hostname = data.hostname
  await host.commit()
  _logger.info(host.dump())
  return host.dump()

@router.delete('/delete/{host_id}')
async def delete(host_id: str):
  host = await Host.get(host_id)
  await host.remove()
  return {}