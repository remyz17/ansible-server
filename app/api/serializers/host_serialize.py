from pydantic import BaseModel
from typing import List, Optional


class HostBase(BaseModel):
    pass


class HostVar(BaseModel):
    key: str
    value: str


class HostResponse(BaseModel):
    _id: str
    hostname: str


class HostGet(HostBase):
    _id: str


class HostGetResponse(BaseModel):
    _id: str
    hostname: str
    group_id: Optional[str]
    hostvars: Optional[List[HostVar]]


class HostGetMulti(HostBase):
    pass


class HostCreate(HostBase):
    hostname: str
    group_id: Optional[str]
    hostvars: List[HostVar] = []


class HostUpdate(HostBase):
    hostname: Optional[str]
    group_id: Optional[str]
    hostvars: List[HostVar] = []
