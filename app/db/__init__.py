from umongo import Instance
from app.db.connect import MongoConnection
from app.core import config

database = MongoConnection(
    config.DB_URI,
    config.DB_PORT,
    'prod' if config.PROD else 'dev'
)

db = database.get_database()
instance = Instance(db)
