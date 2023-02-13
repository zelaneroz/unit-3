import sqlite3
haiku="""Code flows like a stream
Algorithms guide its way
In silence, it solves"""

#Create database with table Words
query = f"""CREATE TABLE if not exists users(
        email text not null unique,
        password text not null,
        username text not null unique
    )"""
connection = sqlite3.Connection("q46.db")
cursor = connection.cursor()
cursor.execute(query)
connection.commit()
# for word in haiku.split():
#     #insert every word and length in the database
#     cursor.execute("SELECT * FROM users")
#query the average of all the lengths
#close database
