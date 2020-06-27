import logging
from bson import ObjectId
from umongo import Document, EmbeddedDocument, fields

from app.db import instance, db

@instance.register
class GroupVar(EmbeddedDocument):
  key = fields.StrField(unique=True)
  value = fields.StrField()

@instance.register
class Group(Document):
  name = fields.StrField(required=True, unique=True)
  parent_id = fields.ReferenceField('Group')
  groupvars = fields.ListField(fields.EmbeddedField(GroupVar))

  @classmethod
  async def get(cls, _id: str):
    if not ObjectId.is_valid(_id):
      return None
    
    return await cls.find_one({'_id': ObjectId(_id)})

  async def add_var(self, var: GroupVar):
    self.groupvars = self.groupvars + [var]