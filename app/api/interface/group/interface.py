from bson import ObjectId

from app.api.interface import BaseInterface
from app.models.group import Group

class GroupInterface(BaseInterface):
  def __init__(self):
    super().__init__(Group)
  
  def create(self, data):
    if isinstance(data.name, str) and data.parent_id:
      return self._model(name=data.name, group_id=ObjectId(data.parent_id)).save()
    elif isinstance(data.name, str):
      return self._model(name=data.name).save()

  def update(self, group_id, data):
    if not isinstance(group_id, str):
      group_id = str(group_id)
    group = self._model.objects.get(id=ObjectId(group_id))
    if data.name and isinstance(data.name, str):
      group.update(name=data.name)
    if data.parent_id and isinstance(data.parent_id, str):
      group.update(parent_id=ObjectId(data.parent_id))
    return group