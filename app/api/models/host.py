from bson import ObjectId
from umongo import Document, fields

from app.core.logger import _logger
from app.db import instance
from app.api.models.group import Group
from app.api.models.inventory import Variable


@instance.register
class Host(Document):
    hostname = fields.StrField(required=True, unique=True)
    group_id = fields.ReferenceField(Group)
    variables = fields.ListField(fields.EmbeddedField(Variable))

    @classmethod
    async def get(cls, _id: str):
        if not ObjectId.is_valid(_id):
            return None

        host = await cls.find_one({"_id": ObjectId(_id)})
        return host

    @classmethod
    async def get_multi(cls, lenght: int = 80):
        cursor = cls.find()
        hosts = []
        for host in await cursor.to_list(length=80):
            hosts.append(host.dump())
        return hosts

    @classmethod
    async def search(cls, hostname: str, limit: int = 5):
        """ cursor = cls.find({ '$text': { '$search': hostname } }) """
        cursor = cls.find({"hostname": {"$regex": hostname}})
        hosts = []
        for host in await cursor.to_list(length=limit):
            hosts.append(host.dump())
        return hosts

    @classmethod
    async def create(cls, data: dict):
        host = cls(**data)
        await host.commit()
        return host

    @classmethod
    async def update_data(cls, _id, data):
        host = await cls.collection.replace_one({"_id": ObjectId(_id)}, data)
        _logger.info(host)

    @classmethod
    async def delete(cls, _id: str):
        host = await cls.get(_id)
        await host.remove()
