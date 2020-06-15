from bson import ObjectId
import logging

from app.api.interface import BaseInterface
from app.models.host import Host

_logger = logging.getLogger('app')

class HostInterface(BaseInterface):
  def __init__(self):
    super().__init__(Host)
  
  def create(self, data):
    if isinstance(data.hostname, str) and data.group_id:
      _logger.info(data.group_id)
      return self._model(hostname=data.hostname, group_id=ObjectId(data.group_id)).save()
    elif isinstance(data.hostname, str):
      return self._model(hostname=data.hostname).save()

  def update(self, host_id, data):
    if not isinstance(host_id, str):
      host_id = str(host_id)
    host = self._model.objects.get(id=ObjectId(host_id))
    _logger.info(host)
    if data.hostname and isinstance(data.hostname, str):
      _logger.info(data.hostname)
      host.update(hostname=data.hostname)
    if data.group_id and isinstance(data.group_id, str):
      _logger.info(host)
      host.update(group_id=ObjectId(data.group_id))
    return host