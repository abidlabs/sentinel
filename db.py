import sqlite3

SCHEMA = [
    'url',
    'outlet',
    'topic',
    'title',
    'date',
    'bias',
]

def create_table_if_not_exists():
    query("""CREATE TABLE IF NOT EXISTS articles (
            url text,
            outlet text,
            topic text,
            title text,
            date text,
            bias integer,
            PRIMARY KEY (url)
            )""")

# update_row(
#     {'url': 'www.google.com',
#         'outlet': 'cnn', 
#         'topic': 'pal',
#         'title': 'haha',
#         'date': 'today',
#         'bias': '5'}
# )

def update_row(entry):
    columns = list(entry.keys())
    values = list(entry.values())
    query_string = "INSERT OR REPLACE INTO articles ({}) VALUES ({})".format(", ".join(columns), "'" + "', '".join(values) + "'")
    print(query_string)
    query(query_string)

def get_all_palestinian_articles():
    query_string = "SELECT * FROM articles"
    return query(query_string)


def query(statement, db_file='db.sqlite3'):
    db = sqlite3.connect(db_file)
    c = db.cursor()
    c.execute(statement)
    db.commit()
    return c.fetchall()
