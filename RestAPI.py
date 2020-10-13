!pip install psycopg2
!pip install flask
!pip install flask_restful

import psycopg2
from flask import Flask, request
from flask_restful import Resource, Api

#Opprett bruker:
def createUser(cur, userID, userName, mail, pw):
    cur.execute("""INSERT INTO "Users" (id, brukernavn, epost, passord) VALUES (%s, %s, %s, %s)""",(str(userID), userName, mail, pw))

#Slett spesifikk bruker:
def delUser(cur, userID):
    cur.execute('DELETE FROM "Users" WHERE id = %s',(str(userID)))

#Hent alle brukere:
def getAll(cur):
    cur.execute('select * from "Users"')

def main():
    #Koble til database:
    conn = psycopg2.connect("dbname=UserDB user=postgres password=test")

    cur = conn.cursor()

    app = Flask(__name__)

    #Lage api:
    api = Api(app)

    #Resource med POST funksjon for å legge til brukere:
    class CreateUser(Resource):
        def post(self):
            par = request.get_json()
            getAll(cur)
            rows = cur.fetchall()
            i = 0
            if len(rows)==0:
                createUser(cur,par[0], par[1], par[2], par[3])
                return {'you sent': par}, 201
            for row in rows:
                if row[0]==par[0]:
                    return 'User already added!'
                else:
                    if i==len(rows)-1:
                        createUser(cur,par[0], par[1], par[2], par[3])
                        return {'you sent': par}, 201
                i+=1

    #Resource med POST funksjon for å slette brukere:
    class DelUser(Resource):
        def post(self,num):
            par = request.get_json()
            getAll(cur)
            rows = cur.fetchall()
            i = 0
            for row in rows:
                if row[0]==par:
                    delUser(cur,int(par))
                    return {'Deleted user number ':num}, 201
                else:
                    if i==len(rows)-1:
                        return 'Non-existent user!'
                i+=1

    #Resource med GET funksjon for å hente alle brukere:
    class Users(Resource):
        def get(self):
            getAll(cur)
            rows = cur.fetchall()
            if len(rows)==0:
                return 'No existing users in database!'
            return rows

    #Resource med GET funksjon for å hente bruker etter ID:
    class UserID(Resource):
        def get(self,num):
            getAll(cur)
            rows = cur.fetchall()
            i = 0
            for row in rows:
                if row[0]==num:
                    return row
                else:
                    if i==len(rows)-1:
                        return 'Non-existent user!'
                i+=1

    api.add_resource(CreateUser, '/users')
    api.add_resource(Users, '/users')
    api.add_resource(UserID, '/users/<int:num>')
    api.add_resource(DelUser, '/users/<int:num>')
    app.run(debug=False)

    cur.close()

    conn.close()

if __name__ == "__main__":
    main()
