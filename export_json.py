import json
from main import conn

data = {}

TABLES = [
    'Artist',
    'The_most_famous_painting',
    'Genre',
    'Bio'
]

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))

        data[table_name] = rows

with open('all_data.json', 'w', encoding="utf-8") as outf:
    json.dump(data, outf, default=str)