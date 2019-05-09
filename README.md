# FlaskAPI

API Training example

## Context for this example

- why API's
  - component design
  - mono-lith vs microservices 

## Assumptions

- Basic Python understanding
- Basic Flask understanding
- Basic HTTP and REST endpoints (GET, POST ...)
- Flask Restful for the API library

## setup

- git clone this repo <https://github.com/cmcc13/FlaskAPI.git>
- setup a virtual env `virtualenv venv`
- open the virtual env `source venv/bin/activate`
- install libraries `pip install requirements.txt`

## run examples

### example 1 - simple API creation and call

- in another terminal run `python test1.py`
- in a browser go to `localhost` click the call api button (it fails)
- in a terminal run `python app1.py`
- in a browser go to `localhost:5000` check that api is healthy
- in a browser go to `localhost` click the call api button (it returns api response)

### example 2 - extend example 1 with argument passing

- in another terminal run `python test2.py`
- in a browser go to `localhost` click the call api button
- in a terminal run `python app2.py`
- in a browser go to `localhost:5000` check that api is healthy

### example 3 - google cloud function as an api

- setup: get a cloud trial account; go to default project; enable billing; enable cloud functions api
- go to cloud functions
- modify the default python function and click create
- test it in a browser or postman
- copy the url to test3.py code
- in a terminal run `python test3.py`
- cleanup: delete your function to avoid ongoing costs

## further reading

- microservices context <https://martinfowler.com/articles/microservices.html>
- REST principles <https://restfulapi.net/>
- for api testing <https://www.getpostman.com/>
- JSON <https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON>
- Flask Restful library <https://flask-restful.readthedocs.io/en/latest/>
- alternatives to flask restful (google FlaskAPI, Django, GraphQL)
- Note that in Flask Restful reqparse is deprecated <https://flask-restful.readthedocs.io/en/0.3.6/reqparse.html> and they suggest using <https://marshmallow.readthedocs.io/en/3.0/>
- cloud serverless api's <https://serverless.com/> <https://aws.amazon.com/lambda/> <https://cloud.google.com/functions/>
