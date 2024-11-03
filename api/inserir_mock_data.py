from sqlite_utils import Database
from datetime import datetime, timedelta
import random

VALOR_VAZAMENTO = 70

DATABASE = 'db.sqlite'
TABELA = 'leituras'

def insert_mock_data(num_entries=500):
    db = Database(DATABASE)

    start_date = datetime.now() - timedelta(days=365)

    for _ in range(num_entries):
        random_date = start_date + timedelta(
            days=random.randint(0, 365),
            hours=random.randint(0, 23),
            minutes=random.randint(0, 59)
        )
        timestamp = random_date.strftime('%Y-%m-%d %H:%M:%S')
        value = f"{random.uniform(0, 100):.2f}"

        db[TABELA].insert({
            "timestamp": timestamp,
            "value": value,
            'vazamento': float(value) > VALOR_VAZAMENTO
        })

    print(f"Inserted {num_entries} mock entries into the '{TABELA}' table in '{DATABASE}'.")

if __name__ == "__main__":
    insert_mock_data(500)
