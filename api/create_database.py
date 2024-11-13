from sqlite_utils import Database

db = Database('db.sqlite')

db["leituras"].create(
    {
        'id': 'INTEGER',
        'timestamp': 'TEXT',
        'value': 'TEXT',
        'vazamento': 'INTEGER',
        'identificador': 'TEXT'
    },
    pk="id",
    if_not_exists=True
)


db['dispostivos'].create(
    {
        'id': 'INTEGER',
        'identificador': 'TEXT'
    },
    pk="id",
    if_not_exists=True
)