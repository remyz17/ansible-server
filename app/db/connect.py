from motor.motor_asyncio import AsyncIOMotorClient
from umongo import Instance
import logging

_logger = logging.getLogger('app')

class MongoConnection(object):

  def __init__(self, uri, port, db):
    self._uri = uri
    self._port = port
    self._db = db

    self._init_conn()

  def _init_conn(self):
    self.client = AsyncIOMotorClient(self._uri, self._port)
    self.db = self.client[self._db]
    _logger.info(
      'connected to mongoDB instance {}'
      .format(
        self.client
      )
    )

  def get_client(self):
    return self.client
  
  def get_database(self):
    return self.db
  
  def close_client(self):
    self.client.close()