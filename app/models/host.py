import logging
from bson import ObjectId
from umongo import Document, fields

from app.db import instance, db
from app.models.group import Group

_logger = logging.getLogger(__name__)

@instance.register
class Host(Document):
  hostname = fields.StrField(required=True, unique=True)
  group_id = fields.ReferenceField(Group)

  @classmethod
  async def get(cls, _id: str):
    if not ObjectId.is_valid(_id):
      return None
    
    return await cls.find_one({'_id': ObjectId(_id)})