from mongoengine import Document, StringField, ReferenceField

class Group(Document):
  name = StringField(required=True, unique=True)
  parent_id = ReferenceField('self')

  """ def parent(self):
    self.objects.get(id=self.parent_id.id) """

  def get_parent_id(self):
    return self.parent_id if self.parent_id else False