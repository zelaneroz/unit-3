import sqlite3
haiku="""Code flows like a stream
Algorithms guide its way
In silence, it solves"""
connection = sqlite3.connect("q46.db")
cursor = connection.cursor()

#Create database with table Words
query = f"""CREATE TABLE if not exists WORDS(
        id integer not null,
        length integer not null,
        word text not null 
    )"""
cursor.execute(query)
connection.commit()
# i=1
# for word in haiku.split():
#     #insert every word and length in the database
#     query= f"INSERT INTO words values({i},{len(word)},'{word}')"
#     i+=1
#     cursor.execute(query)
#     connection.commit()

#query the average of all the lengths
cursor.execute("SELECT avg(length) from WORDS")
print(connection.commit())
#close database
#connection.close()

