import json
def dbdir():
    with open('databaseconfig.json') as db:
            db_dir = json.load(db)

    return db_dir['database_dir']