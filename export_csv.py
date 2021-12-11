import csv
from main import conn

OUTPUT_FILE_T = 'Saltykov_{}.csv'

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
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILE_T.format(table_name), 'w', encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])








