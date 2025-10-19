import sqlite3

connection = sqlite3.connect('movies.db')
cursor = connection.cursor()


#    cursor.execute("""
#       CREATE TABLE IF NOT EXISTS Movies(
#           MovieID INTEGER PRIMARY KEY AUTOINCREMENT,
#            Title TEXT NOT NULL,
#            Director TEXT,
#            Year INTEGER,
#            Rating TEXT,
#            Genre TEXT
#        )
#    """)

cursor.execute("""
    INSERT INTO Movies(Title, Director, Year, Rating, Genre)
    VALUES ('Kpop Demon Hunters', 'Maggie Kang', 2025, 'PG', 'Animation')
""")

movies_to_add = [
    ('The Princess Bride', 'Rob Reiner', 1987, 'PG', 'Fantasy'),
    ('Inception', 'Chrostopher Nolan', 2010, 'PG-13', 'Sci-Fi'),
    ('The Lion King', 'Roger Allers', 1994, 'G', 'Animation'),
    ('The Avengers', 'Joss Whedon', 2012, 'PG-13', 'Action'),
    ('Spirited Away', 'Hayao Miyazaki', 2001, 'PG', 'Animation')

]

cursor.executemany("""
    INSERT INTO Movies (Title, Director, Year, Rating, Genre)
    VALUES(?, ?, ?, ?, ? )
""", movies_to_add)

connection.commit()
cursor.close()
connection.close()