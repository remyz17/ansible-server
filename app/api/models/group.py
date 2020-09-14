import logging
from bson import ObjectId
from umongo import Document, fields

from app.db import instance
from app.api.models.inventory import Variable

_logger = logging.getLogger(__name__)


@instance.register
class Group(Document):
    name = fields.StrField(required=True, unique=True)
    group_id = fields.ReferenceField("Group")
    variables = fields.ListField(fields.EmbeddedField(Variable))

    @classmethod
    async def get(cls, _id: str):
        if not ObjectId.is_valid(_id):
            return None

        group = await cls.find_one({"_id": ObjectId(_id)})
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
        cursor = cls.find({"name": {"$regex": name}})
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
        group = await cls.collection.replace_one({"_id": ObjectId(_id)}, data)
        _logger.info(group)

    @classmethod
    async def delete(cls, _id):
        group = await cls.get(_id)
        await group.remove()
