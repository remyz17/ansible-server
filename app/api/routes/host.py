from fastapi import APIRouter, status

from app.core.logger import _logger
from app.api.serializers import host_serialize
from app.api.models.host import Host
from app.api.models.group import Group

router = APIRouter()


@router.get("/count", status_code=status.HTTP_200_OK)
async def count_docs():
    count = await Host.count_documents()
    return count


@router.get("/get_multi", status_code=status.HTTP_200_OK)
async def get_multi():
    hosts = await Host.get_multi()
    for host in hosts:
        group = None
        if "group_id" in host.keys():
            group = await Group.get(host["group_id"])
        if group:
            host["group"] = group.dump()
    return hosts


@router.get("/get/{host_id}", status_code=status.HTTP_200_OK)
async def get(host_id: str):
    host = await Host.get(host_id)
    host = host.dump()
    group = None
    if "group_id" in host.keys():
        group = await Group.get(host["group_id"])
    if group:
        host["group"] = group.dump()
    return host


@router.get("/search", status_code=status.HTTP_200_OK)
async def search(name: str, limit: int = 5):
    hosts = await Host.search(name, limit)
    return hosts


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create(data: host_serialize.HostCreate):
    host = await Host.create(data.dict(exclude_unset=True))
    return host.dump()


@router.put("/update/{host_id}", status_code=status.HTTP_200_OK)
async def update(host_id: str, data: host_serialize.HostUpdate):
    host = await Host.update_data(host_id, data.dict(exclude_unset=True))
    _logger.info(host)
    return host


@router.delete("/delete/{host_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(host_id: str):
    await Host.delete(host_id)
