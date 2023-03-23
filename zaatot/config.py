import logging
import os

from dotenv import load_dotenv


def get_pg_config():
    if os.getenv("DEV") == "local":
        load_dotenv()
        logging.info("Local config loaded for PostgreSQL")
    host = os.getenv("POSTGRE_SQL_HOST")
    port = os.getenv("POSTGRE_SQL_PORT")
    db = os.getenv("POSTGRE_SQL_DB")
    schema = os.getenv("POSTGRE_SQL_SCHEMA")
    user = os.getenv("POSTGRE_SQL_USER")
    password = os.getenv("POSTGRE_SQL_PASS")
    return host, port, db, schema, user, password
