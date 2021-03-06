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
                #Suksess!:
                createUser(cur,par[0], par[1], par[2], par[3])
                return {'You sent': par}, 201
            for row in rows:
                #Exception for registrering av eksisterende bruker:
                if row[0]==par[0]:
                    return {'Attempted duplicate user registration for user with id': par[0]}, 409
                else:
                    #Suksess!:
                    if i==len(rows)-1:
                        createUser(cur,par[0], par[1], par[2], par[3])
                        return {'You sent': par}, 201
                i+=1

    #Resource med POST funksjon for å slette brukere:
    class DelUser(Resource):
        def post(self,num):
            par = request.get_json()
            getAll(cur)
            rows = cur.fetchall()
            i = 0
            #Exception når det er ingen brukere i databasen:
            if len(rows)==0:
                return 'No resources found!', 404
            for row in rows:
                #Suksess!:
                if row[0]==par:
                    delUser(cur,int(par))
                    return {'Deleted user number ':num}, 202
                else:
                    #Exception hvor bruker med gitt id ikke finnes i databasen:
                    if i==len(rows)-1:
                        return {'No user with id': par}, 404
                i+=1

    #Resource med GET funksjon for å hente alle brukere:
    class Users(Resource):
        def get(self):
            getAll(cur)
            rows = cur.fetchall()
            #Exception når det er ingen brukere i databasen:
            if len(rows)==0:
                return 'No resources found!',404
            #Suksess!:
            return rows, 201

    #Resource med GET funksjon for å hente bruker etter ID:
    class UserID(Resource):
        def get(self,num):
            getAll(cur)
            rows = cur.fetchall()
            i = 0
            #Exception når det er ingen brukere i databasen:
            if len(rows)==0:
                return 'No resources found!', 404
            for row in rows:
                #suksess!:
                if row[0]==num:
                    return row, 201
                #Exception hvor bruker med gitt id ikke finnes i databasen:
                else:
                    if i==len(rows)-1:
                        return {'Non-existent user with id':num},404
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
