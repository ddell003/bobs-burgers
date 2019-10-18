# Bob's Burgers
Python Server VueJs Client - I like burgers and I love the tv show Bob's Burgers and I like programing so I combined the three for a proof of concept!

## About
This is a full stack web application utilizing python as the backend using the micro framework flask and VueJs as the frontend
To demonstrate the utilizations of these frameworks I have made a web application that allows a user to create additional users, 
edit a menu and place orders. This app is far from complete but it demonstrates how to utilize python and flask to make a 
restful API and VueJS as a client.

http://flask.palletsprojects.com/en/1.1.x/


https://vuejs.org/

https://github.com/ddell003/bobs-burgers

## Set Up:
There are two parts to setting up this project. First you need to set up the API which is in the server directory.
Next you need to set up the client which in this APP is a VueJs application.
### Server
To get the python API up and running cd into server and run
```
source env/bin/activate
python app.py
```
 > **NOTE**: You know that you are in a virtual environment as "env" is now showing before the $ in your terminal - (env)$. To exit the virtual environment, use the command `deactivate`. You can reactivate by navigating back to the project directory and running `source env/bin/activate`.
### Client
To get the client running cd into client. Copy and past the generate url into a browser to view it!
```
npm install
npm run serve
```
## Unit Tests
Started basic unit test to demonstrate test driven development using flask

You can also hit the endpoint "setup/run_tests" while the app is running for basic assertions
> **NOTE**: If you started server you will need to exit it first before running tests
```
source env/bin/activate
python test.py
```
## Populating data
* get the server running (python app.py step)
* using postman is a simple solution to interact with this API or you can use curl https://www.getpostman.com/
* you can view all endpoints through importing the .postman_collection.json found in the base of this project into postman

```
# set up data
http://127.0.0.1:5000/setup/setup_db
# or
curl -X GET \
  http://127.0.0.1:5000/setup/setup_db \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 86' \
  -H 'Content-Type: application/json' \
  -H 'Host: 127.0.0.1:5000' \
  -H 'Postman-Token: d26c8556-280a-48a9-9c1d-529ba18ba387,c09a22f9-872b-432b-b69a-06fb3447b216' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'cache-control: no-cache'
```
This endpoints clears the sqlite database and repopulates it with base data needed to utilize the app

## Endpoints
### Users
Get all users:
```
# url
 http://127.0.0.1:5000/api/users

 # curl
 curl -X GET \
  http://127.0.0.1:5000/users \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Host: 127.0.0.1:5000' \
  -H 'Postman-Token: 2d507b10-3b44-42d6-a69e-47e058a3d9a9,3670855c-78fe-494f-a2de-8d61b0255700' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'cache-control: no-cache'
```
Get a user:
```
# url
http://127.0.0.1:5000/api/users/1
# curl
curl -X GET \
  http://127.0.0.1:5000/users/1 \
  -H 'Postman-Token: b90b68a3-1228-4a32-8e51-1ded35158636' \
  -H 'cache-control: no-cache'
```
Create a user:
```
# use postman example or the curl response:
curl -X POST \
  http://127.0.0.1:5000/api/users \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 88' \
  -H 'Content-Type: application/json' \
  -H 'Host: 127.0.0.1:5000' \
  -H 'Postman-Token: 230d5dad-f8dc-41e4-9e2a-81bbe9eba4d5,aa613842-8a17-4f79-8615-8040148a22f2' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'cache-control: no-cache' \
  -d '{
	"first_name":"bobss",
	"last_name":"Belchers",
	"email":"bob@bobsburgers.gmail.com"
}'

```
Update a user:
```
curl -X PUT \
  http://127.0.0.1:5000/api/users/1 \
  -H 'Accept: */*' \
  -H 'Accept-Encoding: gzip, deflate' \
  -H 'Cache-Control: no-cache' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 88' \
  -H 'Content-Type: application/json' \
  -H 'Host: 127.0.0.1:5000' \
  -H 'Postman-Token: dbebd750-83e9-47d6-96cb-4fcbd99a46ef,fb90e9d6-9432-4b48-bdf4-6e9ae1d43bc7' \
  -H 'User-Agent: PostmanRuntime/7.17.1' \
  -H 'cache-control: no-cache' \
  -d '{
	"first_name":"bobss",
	"last_name":"Belchers",
	"email":"bob@bobsburgers.gmail.com"
}'
```

Delete a user:
```
curl -X DELETE \
  http://127.0.0.1:5000/api/users/1 \
  -H 'Content-Type: application/json' \
  -H 'Postman-Token: bb08c974-a78c-438b-a03b-7c76271e1529' \
  -H 'cache-control: no-cache' \
  -d '{
	"first_name":"bobss",
	"last_name":"Belcher",
	"email":"bob@bobsburgers.gmail.com"
}'
```
