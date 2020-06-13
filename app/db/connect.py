from mongoengine import connect
import logging

_logger = logging.getLogger('app')

class MongoConnection(object):

  def __init__(self, uri, port, db):
    self._uri = uri
    self._port = port
    self._db = db

    self._init_conn()

  def _init_conn(self):
    connect(self._db, host=self._uri, port=self._port)
    _logger.info(
      'connected to mongoDB instance at {} on port {}'
      .format(
        self._uri, self._port
      )
    )