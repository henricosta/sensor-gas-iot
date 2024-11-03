from sqlite_utils import Database

db = Database('db.sqlite')

db["leituras"].create(
    {
        'id': 'INTEGER',
        'timestamp': 'TEXT',
        'value': 'TEXT',
        'vazamento': 'INTEGER'
    },
    pk="id",
    if_not_exists=True
)
