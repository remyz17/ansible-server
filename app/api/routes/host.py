from fastapi import APIRouter, status

from app.core.logger import _logger
from app.api.serializers import host_serialize
from app.api.models.host import Host

router = APIRouter()


@router.get("/get_multi", status_code=status.HTTP_200_OK)
async def get_multi():
    hosts = await Host.get_multi()
    return hosts


@router.get(
    "/get/{host_id}",
    # response_model=host_serialize.HostGetResponse,
    status_code=status.HTTP_200_OK,
)
async def get(host_id: str):
    host = await Host.get(host_id)
    return host


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create(data: host_serialize.HostCreate):
    host = await Host.create(data.dict(exclude_unset=True))
    _logger.info(host)
    return host


@router.put("/update/{host_id}")
async def update(host_id: str, data: host_serialize.HostUpdate):
    host = await Host.update_data(host_id, data.dict(exclude_unset=True))
    _logger.info(host)
    return host


@router.delete("/delete/{host_id}")
async def delete(host_id: str):
    host = await Host.get(host_id)
    await host.remove()
    return {}
