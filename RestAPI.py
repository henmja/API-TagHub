!pip install psycopg2
!pip install requests

import psycopg2

#Opprett bruker:
def createUser(cur):
    cur.execute("""INSERT INTO "Users" (id, brukernavn, epost, passord) VALUES (3, 'x', 'y', 'z')""")

#Hent spesifikk bruker:
def getUser(cur, userID):
    cur.execute('select * from "Users" where id = %s',(str(userID)))

#Slett spesifikk bruker:
def delUser(cur, userID):
    cur.execute('DELETE FROM "Users" WHERE id = %s',(str(userID)))

#Hent alle brukere:
def getAll(cur):
    cur.execute('select * from "Users"')

def printRows(rows):
    for r in rows:
        print(r)


def main():
    conn = psycopg2.connect("dbname=UserDB user=postgres password=test")

    #port = 5432

    cur = conn.cursor()
    createUser(cur)
    getUser(cur,3)
    rows = cur.fetchall()
    printRows(rows)


    delUser(cur,3)
    getAll(cur)
    rows = cur.fetchall()
    printRows(rows)

    cur.close()

    conn.close()

if __name__ == "__main__":
    main()
