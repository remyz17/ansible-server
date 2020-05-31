from pymodm import MongoModel, fields

class Hosts(MongoModel):
  name = fields.CharField()