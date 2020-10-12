!pip install psycopg2

import psycopg2

conn = psycopg2.connect("dbname=UserDB user=postgres password=test")

#port = 5432

cur = conn.cursor()

#Opprett bruker:
def createUser():
    cur.execute("""INSERT INTO "Users" (id, brukernavn, epost, passord) VALUES (3, 'x', 'y', 'z')""")

#Hent spesifikk bruker:
def getUser(userID):
    cur.execute('select * from "Users" where id = %s',(str(userID)))

createUser()
getUser(3)

rows = cur.fetchall()

for r in rows:
    print(r)






#Slett spesifikk bruker:
def delUser(userID):
    cur.execute('DELETE FROM "Users" WHERE id = %s',(str(userID)))

#Hent alle brukere:
def getAll():
    cur.execute('select * from "Users"')

delUser(3)
getAll()

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()

conn.close()
