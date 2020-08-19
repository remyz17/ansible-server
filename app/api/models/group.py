import logging
from logging import log
from bson import ObjectId
from umongo import Document, EmbeddedDocument, fields

from app.db import instance, db

_logger = logging.getLogger(__name__)


@instance.register
class GroupVar(EmbeddedDocument):
    key = fields.StrField()
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

        group = await cls.find_one({'_id': ObjectId(_id)})
        return group

    @classmethod
    async def get_multi(cls, lenght=80):
        cursor = cls.find()
        groups = []
        for group in await cursor.to_list(length=80):
            groups.append(group.dump())
        return groups
    
    @classmethod
    async def search(cls, name: str, limit: int = 5):
        cursor = cls.find({'name': { '$regex': name }})
        groups = []
        for group in await cursor.to_list(length=limit):
            groups.append(group.dump())
        return groups

    @classmethod
    async def create(cls, data):
        group = cls(**data)
        await group.commit()
        return group

    @classmethod
    async def update_data(cls, _id, data):
        group = await cls.collection.update_one(
            {'_id': ObjectId(_id)},
            {'$set': data}
        )
        _logger.info(group)
    
    @classmethod
    async def delete(cls, _id):
        group = await cls.get(_id)
        await group.remove()
