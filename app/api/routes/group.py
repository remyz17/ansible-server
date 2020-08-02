from fastapi import APIRouter

from app.core.logger import _logger
from app.api.serializers import group_serialize
from app.api.models.host import Host
from app.api.models.group import Group, GroupVar

router = APIRouter()


@router.get('/get_multi')
async def get_multi():
    cursor = Group.find()
    groups = [host.dump() for host in await cursor.to_list(length=80)]
    _logger.info(groups)
    return groups


@router.get('/get/{group_id}')
async def get(group_id: str):
    group = await Group.get(group_id)
    _logger.info(group.dump())
    return group.dump()


@router.post('/create')
async def create(data: group_serialize.GroupCreate):
    group = Group(name=data.name, groupvars=[])
    if hasattr(data, 'parent_id'):
        parent = await Group.get(data.parent_id)
        _logger.info(parent)
        if parent:
            group.parent_id = parent
    if hasattr(data, 'groupvars'):
        for var in data.groupvars:
            new_var = GroupVar(key=var.key, value=var.value)
            await group.add_var(new_var)
    await group.commit()
    return group.dump()


@router.put('/update/{group_id}')
async def update(group_id: str, data: group_serialize.GroupUpdate):
    group = await Group.get(group_id)
    group = await group.update(name=data.name)
    _logger.info(group.dump())
    return group.dump()


@router.delete('/delete/{group_id}')
async def delete(group_id: str):
    group = await Group.get(group_id)
    await group.remove()
    return {}
