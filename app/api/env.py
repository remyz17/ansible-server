from umongo import Instance

from app.db.connect import MongoConnection
from app.core import config

class Env(object):

  _conn = False
  _instance = False

  def __init__(self, production=False):
    self._prod = production

  @property
  def is_prod(self):
    return self._prod
  
  def _init_db(self):
    self._conn = MongoConnection(
      config.DB_URI,
      config.DB_PORT,
      'prod' if self.is_prod else 'dev'
    )
  
  def _get_instance(self):
    if self._conn:
      if isinstance(self._instance, Instance):
        return self._instance
      else:
        self._instance = Instance(self._conn.get_database())

