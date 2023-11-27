import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Fol5089**",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    #FIRST QUERY display studio records
    cursor.execute("SELECT * FROM studio")
    studios = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for studio in studios:
        print("Studio ID: {}\nStudio Name: {}\n".format(studio[0], studio[1]))
    print()

    #SECOND QUERY display genre records
    cursor.execute("SELECT * FROM genre")
    genres = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for genre in genres:
        print("Genre ID: {}\nGenre Name: {}\n".format(genre[0], genre[1]))
    print()

    #THIRD QUERY display movie names for movies with run times less than two hours
    cursor.execute("SELECT * FROM film WHERE film_runtime < 120")
    films = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for film in films:
        print("Film Name: {}\nRuntime: {}\n".format(film[1], film[3]))
    print()

    #FOURTH QUERY display film name and director in order of director
    cursor.execute("SELECT * FROM film ORDER BY film_director")
    films = cursor.fetchall()
    print("-- DISPLAYING Director RECORDS in Order --")
    for film in films:
        print("Film Name: {}\nDirector: {}\n".format(film[1], film[4]))
    print()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print(" The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")
    else:
        print(err)

finally:
    db.close()