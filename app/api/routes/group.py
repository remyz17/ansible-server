from fastapi import APIRouter, status

from app.core.logger import _logger
from app.api.serializers import group_serialize
from app.api.models.group import Group

router = APIRouter()


@router.get("/count", status_code=status.HTTP_200_OK)
async def count_docs():
    count = await Group.count_documents()
    return count


@router.get("/get_multi")
async def get_multi():
    groups = await Group.get_multi()
    for group in groups:
        parent = None
        if "parent_id" in group.keys():
            parent = await Group.get(group["parent_id"])
        if parent:
            group["parent"] = parent.dump()
    return groups


@router.get("/get/{group_id}")
async def get(group_id: str):
    group = await Group.get(group_id)
    group = group.dump()
    parent = None
    if "parent_id" in group.keys():
        parent = await Group.get(group["parent_id"])
    if parent:
        group["parent"] = parent.dump()
    return group


@router.get("/search")
async def search(name: str, limit: int = 5):
    groups = await Group.search(name, limit)
    _logger.info(groups)
    return groups


@router.post("/create")
async def create(data: group_serialize.GroupCreate):
    group = await Group.create(data.dict(exclude_unset=True))
    return group.dump()


@router.put("/update/{group_id}")
async def update(group_id: str, data: group_serialize.GroupUpdate):
    group = await Group.update_data(group_id, data.dict(exclude_unset=True))
    _logger.info(group)
    return group


@router.delete("/delete/{group_id}")
async def delete(group_id: str):
    await Group.delete(group_id)
