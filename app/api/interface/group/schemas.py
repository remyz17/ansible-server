from pydantic import BaseModel
from typing import List, Optional

class GroupBase(BaseModel):
  pass

class GroupCreate(GroupBase):
  name: str

class GroupUpdate(GroupBase):
  name: str