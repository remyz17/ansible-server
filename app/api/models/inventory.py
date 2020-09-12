from umongo import EmbeddedDocument, fields
from app.db import instance


@instance.register
class Variable(EmbeddedDocument):
    key = fields.StrField()
    value = fields.StrField()
