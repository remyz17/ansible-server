from app.models.host import Host
from app.models.group import Group

async def ensure_indexes():
  await Host.ensure_indexes()
  await Group.ensure_indexes()