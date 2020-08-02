from fastapi import APIRouter, status
from starlette.status import HTTP_201_CREATED

from app.core.logger import _logger
from app.api.serializers import host_serialize
from app.api.models.host import Host, HostVar
from app.api.models.group import Group

router = APIRouter()

@router.get(
  '/get_multi',
  status_code=status.HTTP_200_OK
)
async def get_multi():
  hosts = await Host.get_multi()
  return hosts

@router.get(
  '/get/{host_id}',
  # response_model=host_serialize.HostGetResponse,
  status_code=status.HTTP_200_OK
)
async def get(host_id: str):
  host = await Host.get(host_id)
  return host

@router.post(
  '/create',
  status_code=status.HTTP_201_CREATED
)
async def create(data: host_serialize.HostCreate):
  _logger.info(data.json())
  host = await Host.create(data.dict())
  """ host = Host(hostname=data.hostname, hostvars=[{'key': 'ahah', 'value': 'test val'}])
  if hasattr(data, 'group_id'):
    group = await Group.get(data.group_id)
    if group:
      host.group_id = group
  if hasattr(data, 'hostvars'):
    for var in data.hostvars:
      new_var = HostVar(key=var.key, value=var.value)
      await host.add_var(new_var)
  await host.commit()
  return host.dump() """

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