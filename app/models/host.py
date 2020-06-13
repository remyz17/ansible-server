from mongoengine import Document, StringField, ReferenceField

from app.models.group import Group
import logging

_logger = logging.getLogger(__name__)

class Host(Document):
  hostname = StringField(required=True, unique=True)
  group_id = ReferenceField('Group')

  def group(self):
    _logger.info(type(self.group_id.id))
    return Group.objects.get(id=self.group_id.id)