from pydantic import BaseModel
from typing import List, Optional

class HostBase(BaseModel):
  pass

class HostGet(HostBase):
  _id: str

class HostGetMulti(HostBase):
  pass

class HostCreate(HostBase):
  hostname: str
  group_id: Optional[str]

class HostUpdate(HostBase):
  hostname: Optional[str]
  group_id: Optional[str]