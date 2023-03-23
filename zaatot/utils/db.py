def create_sqlalchemy_url(host, port, db, schema, user, pwd):
    sql_alchemy_db_url = f"postgresql://{user}:{pwd}@{host}:{port}/{db}?options=-csearch_path%3D{schema}"
    return sql_alchemy_db_url
