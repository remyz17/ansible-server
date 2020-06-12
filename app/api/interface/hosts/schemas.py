from pydantic import BaseModel
from typing import List, Optional

class HostBase(BaseModel):
  pass

class HostCreate(HostBase):
  name: str

class HostUpdate(HostBase):
  name: str