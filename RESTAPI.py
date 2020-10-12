!pip install psycopg2

import psycopg2

conn = psycopg2.connect("dbname=UserDB user=postgres password=test")

#port = 5432

cur = conn.cursor()

#Hent spesifikk bruker:
#cur.execute('select <id> from "Users"')

#Opprett bruker:
cur.execute("""INSERT INTO "Users" (id, brukernavn, epost, passord) VALUES (3, 'x', 'y', 'z')""")

#Slett spesifikk bruker:
cur.execute('DELETE FROM "Users" WHERE id = 3')

#Hent alle brukere:
cur.execute('select * from "Users"')
rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()

conn.close()
