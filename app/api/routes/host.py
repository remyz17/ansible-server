from fastapi import APIRouter
import logging

from app.api.interface.host import schemas
from app.models.host import Host
from app.models.group import Group

_logger = logging.getLogger('app')
router = APIRouter()

@router.get('/get_multi')
async def get_multi():
  for host in Host.objects():
    a = host.group()
    _logger.info(a.name)
    """ group = Group.objects(id=).all() """
    """ _logger.info(group) """
  return {}

@router.get('/get/{host_id}')
async def get(host_id: str):
  _logger.info('host %s' % host_id)
  return {}

@router.post('/create')
async def create(data: schemas.HostCreate):
  _logger.info(data)
  group = Group(name='test-group').save()
  host = Host(hostname=data.hostname, group_id=group).save()
  _logger.info(host)
  return {}

@router.put('/update/{host_id}')
async def update(host_id: str, data: schemas.HostUpdate):
  _logger.info(host_id)
  _logger.info(data)
  return {}

@router.delete('/delete/{host_id}')
async def delete(host_id: str):
  return {}