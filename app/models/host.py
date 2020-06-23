import logging
from bson import ObjectId
from umongo import Document, EmbeddedDocument, fields

from app.db import instance, db
from app.models.group import Group

_logger = logging.getLogger(__name__)

@instance.register
class HostVar(EmbeddedDocument):
  key = fields.StrField(unique=True)
  value = fields.StrField()

@instance.register
class Host(Document):
  hostname = fields.StrField(required=True, unique=True)
  group_id = fields.ReferenceField(Group)
  _vars = fields.ListField(fields.EmbeddedField(HostVar))

  @classmethod
  async def get(cls, _id: str):
    if not ObjectId.is_valid(_id):
      return None
    
    return await cls.find_one({'_id': ObjectId(_id)})
  
  async def add_var(self, var: HostVar):
    self._vars = self._vars + [var]
