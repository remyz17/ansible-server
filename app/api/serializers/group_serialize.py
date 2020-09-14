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
    group_id: Optional[str]
    variables: List[GroupVar] = []


class GroupUpdate(GroupBase):
    name: Optional[str]
    group_id: Optional[str]
    variables: List[GroupVar] = []
