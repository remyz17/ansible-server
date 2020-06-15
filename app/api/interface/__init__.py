from bson import ObjectId
import logging

_logger = logging.getLogger('app')

class BaseInterface(object):
  def __init__(self, model):
    self._model = model

  def get(self, _id):
    return self._model.objects.get(id=ObjectId(_id))

  def get_multi(self):
    _logger.info(self._model.objects)
    return self._model.objects

  def delete(self, _id):
    return self._model.objects.get(id=ObjectId(_id)).delete()