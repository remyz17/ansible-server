from pymodm import connect
import logging

_logger = logging.getLogger('app')

class MongoConnection(object):

  def __init__(self, uri, db):
    self._uri = uri
    self._db = db
    self._alias = '{}-conn'.format(db)

    self._init_conn()

  def _init_conn(self):
    url = '{uri}{db}'.format(uri=self._uri, db=self._db)
    _logger.info('connected to mongoDB instance at {}'.format(url))
    connect(url)