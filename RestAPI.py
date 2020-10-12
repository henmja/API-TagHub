!pip install psycopg2
!pip install flask
!pip install flask_restful

import psycopg2
#import requests
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Opprett bruker:
def createUser(cur):
    cur.execute("""INSERT INTO "Users" (id, brukernavn, epost, passord) VALUES (3, 'x', 'y', 'z')""")

#Hent spesifikk bruker:
#def getUser(cur, userID):
#    cur.execute('select * from "Users" where id = %s',(str(userID)))

#Slett spesifikk bruker:
def delUser(cur, userID):
    cur.execute('DELETE FROM "Users" WHERE id = %s',(str(userID)))

#Hent alle brukere:
def getAll(cur):
    cur.execute('select * from "Users"')

#def printRows(rows):
#    for r in rows:
#        print(r)


def main():
    conn = psycopg2.connect("dbname=UserDB user=postgres password=Ageofconan3")

    #port = 5432

    cur = conn.cursor()
    createUser(cur)
    #getUser(cur,3)
    #rows = cur.fetchall()
    #printRows(rows)


    delUser(cur,3)
    getAll(cur)
    rows = cur.fetchall()
    #printRows(rows)
    class CreateUser(Resource):
        def post(self):
            some_json = request.get_json()
            return {'you sent': some_json}, 201

    class DelUser(Resource):
        def post(self):
            some_json = request.get_json()
            return {'you sent': some_json}, 201

    class Users(Resource):
        def get(self):
            return rows

    class UserID(Resource):
        def get(self,num):
            i = 0
            for row in rows:
                if row[0]==num:
                    return row
                else:
                    if i==len(rows)-1:
                        return 'Non-existent user!'
                i+=1

    api.add_resource(Users, '/users')
    api.add_resource(UserID, '/users/<int:num>')
    app.run(debug=False)

    cur.close()

    conn.close()

if __name__ == "__main__":
    main()
