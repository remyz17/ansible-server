import logging
from bson import ObjectId
from umongo import Document, fields

from app.db import instance, db

@instance.register
class Group(Document):
  name = fields.StrField(required=True, unique=True)
  parent_id = fields.ReferenceField('Group')

  @classmethod
  async def get(cls, _id: str):
    if not ObjectId.is_valid(_id):
      return None
    
    return await cls.find_one({'_id': ObjectId(_id)})