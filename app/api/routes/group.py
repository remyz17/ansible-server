from fastapi import APIRouter
import logging

from app.api.interface.group import schemas
from app.models.host import Host
from app.models.group import Group

_logger = logging.getLogger('app')
router = APIRouter()

@router.get('/get_multi')
async def get_multi():
  for group in Group.objects():
    if group.get_parent_id():
      _logger.info(group.get_parent_id().name)
  return {}

@router.get('/get/{group_id}')
async def get(group_id: str):
  _logger.info('group %s' % group_id)
  return {}

@router.post('/create')
async def create(data: schemas.GroupCreate):
  _logger.info(data)
  group = Group(name=data.name).save()
  new_group = Group(name='shsjkshs', parent_id=group).save()
  _logger.info(new_group)
  return {}

@router.put('/update/{group_id}')
async def update(group_id: str, data: schemas.GroupUpdate):
  _logger.info(group_id)
  _logger.info(data)
  return {}

@router.delete('/delete/{group_id}')
async def delete(group_id: str):
  return {}