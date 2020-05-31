from app.db.connect import MongoConnection
from app.core import config

class Env(object):

  def __init__(self, production=False):
    self._prod = production
    self._init_db()

  @property
  def is_prod(self):
    return self._prod
  
  def _init_db(self):
    if self.is_prod:
      MongoConnection(config.DB_URI, 'prod')
    else:
      MongoConnection(config.DB_URI, 'dev')
