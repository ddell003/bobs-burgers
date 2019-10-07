# bobs-burgers
Python Server VueJs Client

## Server
to get the python server up and running cd into server and run
```
source env/bin/activate
python app.py
```

## Populating data
* using postman is a simple solution to interact with this API or you can use curl https://www.getpostman.com/

```
# set up data
http://127.0.0.1:5000/users
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
