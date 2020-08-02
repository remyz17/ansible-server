from pydantic import BaseModel
from typing import List, Optional


class GroupBase(BaseModel):
    pass


class GroupGet(GroupBase):
    _id: str


class GroupGetMulti(GroupBase):
    pass


class GroupVar(BaseModel):
    key: str
    value: str


class GroupCreate(GroupBase):
    name: str
    parent_id: Optional[str]
    groupvars: List[GroupVar] = []


class GroupUpdate(GroupBase):
    name: Optional[str]
    parent_id: Optional[str]
    groupvars: List[GroupVar] = []
