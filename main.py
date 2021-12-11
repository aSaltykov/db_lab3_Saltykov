import psycopg2
import matplotlib.pyplot as plt

username = 'postgres'
password = 'andron112233andy'
database = 'lab_2_database'
host = 'localhost'
port = '5432'

query_1 = '''
CREATE VIEW PaintingArtist AS SELECT artist_name, COUNT(painting_name) FROM the_most_famous_painting LEFT JOIN  artist ON the_most_famous_painting.painting_id =  artist.artist_id GROUP BY artist_name
'''

query_2 = '''
CREATE VIEW GenreBio AS SELECT genre, COUNT(genre_id) FROM genre INNER JOIN bio USING(genre_id) GROUP BY genre
'''
query_3 = '''
CREATE VIEW GenreAboutBio AS SELECT genre_name, COUNT(about_bio) FROM bio LEFT JOIN genre ON bio.genre_id = genre.genre_id GROUP BY genre_name
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
with conn:
    cur = conn.cursor()
    cur.execute('DROP VIEW IF EXISTS PaintingArtist')

    cur.execute(query_1)
    cur.execute('SELECT * FROM PaintingArtist')
    item_names_2 = []
    item_values_2 = []
    for elements_2 in cur:
        item_names_2.append(elements_2[0].replace(' ', ''))
        item_values_2.append(elements_2[1])
    plt.bar(item_names_2,item_values_2)
    plt.yticks(item_values_2)
    plt.xticks(item_names_2,fontsize=8)
    plt.xlabel('Художники')
    plt.ylabel('Кількість картин згаданих у таблиці')
    plt.show()

    cur.execute('DROP VIEW IF EXISTS GenreBio')
    cur.execute(query_2)
    cur.execute('SELECT * FROM GenreBio')
    item_names = []
    item_values = []
    for elements in cur:
        item_names.append(elements[0].replace(' ',''))
        item_values.append(elements[1])
    fig, ax = plt.subplots()
    ax.pie([item_values[i]/sum(item_values)*100 for i in range(len(item_values))], labels= item_names, autopct='%.2f%%')
    plt.show()

    cur.execute('DROP VIEW IF EXISTS GenreAboutBio')
    cur.execute(query_3)
    cur.execute('SELECT * FROM GenreAboutBio')
    item_names_1 = []
    item_values_1 = []
    for elements_1 in cur:
        item_names_1.append(elements_1[0].replace(' ', ''))
        item_values_1.append(elements_1[1])
    plt.xlim([0,5])
    plt.scatter(item_values_1, item_names_1, color ="deeppink")
    plt.show()




