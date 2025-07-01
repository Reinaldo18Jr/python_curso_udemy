import sqlite3
from pathlib import Path

# obs -> __file__ "esse arquivo" ; parent "essa pasta"
ROOT_DIR = Path(__file__).parent

DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# CRUD => Create - Read - Update - Delete
# SQL => INSERT - SELECT - UPDATE - DELETE

# CUIDADO: fazendo delete sem WHERE
# cursor.execute(
#     f'DELETE FROM {TABLE_NAME}'
# )

# DELETE 'mais cuidadoso'
# cursor.execute(
#     f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
# )
# connection.commit()

# Cria a tabela
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Registrar valores nas colunas da tabela
sql = (
    F'INSERT INTO {TABLE_NAME} ' 
    '(name, weight) '
    'VALUES '
    # '(?, ?)'
    '(:nome, :peso)'
)
# cursor.execute(sql, ['Rei', 5])
# cursor.executemany(sql, [['Rei', 33], ['Juninho', 9]])
cursor.execute(sql, {'nome': 'Rei', 'peso': 5})
cursor.executemany(sql, (
    {'nome': 'Sem Nome', 'peso': 5},
    {'nome': 'Junior', 'peso': 11},
    {'nome': 'Souza', 'peso': 78},
    {'nome': 'Ana', 'peso': 1},
))
connection.commit()


if __name__ == '__main__':
    print(sql)

    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = "3"')
    cursor.execute(f'DELETE FROM {TABLE_NAME} WHERE id = 1')
    connection.commit()

    cursor.execute(
    f'UPDATE {TABLE_NAME} '
    'SET name="outro", weight=67.89 '
    'WHERE id = 5'
    )
    connection.commit()

    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    for row in cursor.fetchall():
        _id, name, weight = row
        print(_id, name, weight)

    cursor.close()
    connection.close()
