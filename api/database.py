from sqlite_utils import Database

DATABASE = 'db.sqlite'
TABELA = 'leituras'


def get_database_connection():
    return Database(DATABASE)


def salvar_dados_leitura(value, vazamento, timestamp):
    db = get_database_connection()
    db[TABELA].insert({
        "value": value,
        "timestamp": timestamp,
        'vazamento': vazamento
    })


def get_all_leituras():
    db = get_database_connection()
    rows = list(db[TABELA].rows)
    return rows


def get_leituras(page=1, per_page=100):
    db = get_database_connection()
    offset = (page - 1) * per_page
    rows = list(db[TABELA].rows_where(
        order_by="timestamp DESC", limit=per_page, offset=offset))
    return rows


def get_ultima_leitura():
    db = get_database_connection()
    row = next(db[TABELA].rows_where(order_by="timestamp DESC", limit=1), None)

    return row
