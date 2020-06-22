import logging
from bson import ObjectId
from umongo import Document, EmbeddedDocument, fields

from app.db import instance, db

@instance.register
class GroupVar(EmbeddedDocument):
  key = fields.StringField(required=True, unique=True)
  value = fields.StrField(required=True)

@instance.register
class Group(Document):
  name = fields.StrField(required=True, unique=True)
  parent_id = fields.ReferenceField('Group')
  _var = fields.EmbeddedField(GroupVar)

  @classmethod
  async def get(cls, _id: str):
    if not ObjectId.is_valid(_id):
      return None
    
    return await cls.find_one({'_id': ObjectId(_id)})