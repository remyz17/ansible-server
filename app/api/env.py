class Env(object):
  def __init__(self, production=False):
    self._prod = production

  @property
  def is_prod(self):
    return self._prod