from pydantic import BaseModel
from typing import List, Optional

class HostBase(BaseModel):
  pass

class HostCreate(HostBase):
  hostname: str

class HostUpdate(HostBase):
  hostname: str