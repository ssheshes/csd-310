import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Fol5089**",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

db = mysql.connector.connect(**config)
cursor = db.cursor()

def show_films(cursor, title):
    try:
        cursor.execute("select film_name as 'Name', film_director as 'Director', genre_name as 'Genre', studio_name as 'Studio Name' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id;")
        films = cursor.fetchall()
        print("\n== {} ==".format(title))
        for film in films:
            print("Film Name: {}\nDirector: {}\nGenre: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print(" The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(" The specified database does not exist")
        else:
            print(err)


###output original table

show_films(cursor, "DISPLAYING FILMS")

###add new film

cursor.execute("INSERT INTO studio (studio_id, studio_name) VALUES (4, 'Studio Ghibli')")
cursor.execute("INSERT INTO genre (genre_id, genre_name) VALUES (4, 'Animation')")
cursor.execute("INSERT INTO film (film_id, film_name, film_releaseDate, film_runTime, film_director, studio_id, genre_id) VALUES (4, 'Spirited Away', 2001, 125, 'Hayao Miyazaki', 4, 4);")
show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

###update "Alien" into Horror genre

cursor.execute("UPDATE film SET genre_id=1 WHERE film_name= 'Alien';")
show_films(cursor, "DISPLAYING FILMS AFTER UPDATE -Changed Alien to Horror")

###delete the movie Gladiator

cursor.execute("delete from film where film_name='Gladiator';")
show_films(cursor, "DISPLAYING FILMS AFTER DELETE")

db.close()