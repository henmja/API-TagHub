import psycopg2

conn = psycopg2.connect("dbname=UserDB user=postgres password=Ageofconan3")

#port = 5432

cur = conn.cursor()

cur.execute('select * from "Users"')

rows = cur.fetchall()

for r in rows:
    print(r)

cur.close()

conn.close()
