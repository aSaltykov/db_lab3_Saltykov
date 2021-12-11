import csv
from main import conn

INPUT_CSV_FILE = "lab_3_artists.csv"

create = ''' 
CREATE TABLE ORIGIN(
	id int NOT NULL PRIMARY KEY,
	name char(50),
	paintings char(1000)
)
'''

delete = '''
DELETE FROM ORIGIN
'''

insert = '''
INSERT INTO ORIGIN (id, name, paintings) VALUES (%s, %s, %s)
'''


with conn:
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS ORIGIN')
    cur.execute(create)
    cur.execute(delete)
    with open(INPUT_CSV_FILE, 'r', encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for idx, row in enumerate(reader):
            data = (row["id"], row["name"], row["paintings"])
            cur.execute(insert, data)

    conn.commit()















