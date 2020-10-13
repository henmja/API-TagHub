# Restful API

Restful API for viewing/editing users in a PostgreSQL database using Python.

The PostgreSQL database was created using pgAdmin 4.

The Restful API was created using the flask and flask_restful frameworks.

## Compilation Scenario:

### Server Side:

python RestAPI.py

### Client Side:

#### Get all users:
curl http://127.0.0.1:5000/users

#### Get user by index:
curl http://127.0.0.1:5000/users/1

#### Add user:
curl -H "Content-Type: application/json" -X POST -d '[4, "abc", "def", "ghi"]' http://127.0.0.1:5000/users

#### Delete user:
curl -H "Content-Type: application/json" -X POST -d '1' http://127.0.0.1:5000/users/1
