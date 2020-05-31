from fastapi import APIRouter
import logging

from app.models.hosts import Hosts

_logger = logging.getLogger('app')

router = APIRouter()

@router.get('/index')
async def index():
  ret = {}
  for host in Hosts.objects.all():
    ret[str(host._id)] = host.name
  _logger.info(ret)
  return ret

@router.post('/create/{hostname}')
async def create(hostname: str):
  Hosts(hostname).save()
  return {}