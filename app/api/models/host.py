from bson import ObjectId
from umongo import Document, EmbeddedDocument, fields

from app.core.logger import _logger
from app.db import instance, db
from app.api.models.group import Group


@instance.register
class HostVar(EmbeddedDocument):
    key = fields.StrField(unique=True)
    value = fields.StrField()


@instance.register
class Host(Document):
    hostname = fields.StrField(required=True, unique=True)
    group_id = fields.ReferenceField(Group)
    hostvars = fields.ListField(fields.EmbeddedField(HostVar))

    @classmethod
    async def get(cls, _id: str):
        if not ObjectId.is_valid(_id):
            return None

        host = await cls.find_one({'_id': ObjectId(_id)})
        host = host.dump()
        if 'group_id' in host.keys():
            group = await Group.get(host['group_id'])
            host['group'] = group.dump()
        return host

    @classmethod
    async def get_multi(cls, lenght=80):
        cursor = cls.find()
        hosts = []
        for host in await cursor.to_list(length=80):
            host = host.dump()
            if 'group_id' in host.keys():
                group = await Group.get(host['group_id'])
                host['group'] = group.dump()
            hosts.append(host)
        return hosts

    @classmethod
    async def create(cls, data):
        host = cls(**data)
        await host.commit()
        return host

    @classmethod
    async def update_data(cls, _id, data):
        _logger.info(data)
        host = await cls.collection.update_one(
            {'_id': ObjectId(_id)},
            {'$set': data}
        )
        _logger.info(host)