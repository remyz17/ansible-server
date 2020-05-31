from fastapi import APIRouter
import logging

from app.models.hosts import Hosts

_logger = logging.getLogger('app')

router = APIRouter()

@router.get('/test')
async def test():
  res = Hosts('ahah').save()
  _logger.info(res)
  for host in Hosts.objects.all():
    _logger.info(host._id)
    _logger.info(host.name)
  return {'test': True}