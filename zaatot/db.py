from sqlalchemy import MetaData

from zaatot.config import get_pg_config
from zaatot.utils.db import create_sqlalchemy_url

host, port, db, schema, user, pwd = get_pg_config()
SQLALCHEMY_DB_URL = create_sqlalchemy_url(host, port, db, schema, user, pwd)
