# FlaskAPI
API Training example

## Context for this example

- why API's
    - component design
    - mono-lith vs microservices 

## Assumptions

- Basic Python understanding
- Basic Flask understanding
- HTTP and REST endpoints
- Flask Restful for the API library 

## setup

- git clone this repo https://github.com/cmcc13/FlaskAPI.git
- setup a virtual env `virtualenv venv`
- open the virtual env `source venv/bin/activate`
- install libraries `pip install requirements.txt`

## run examples

### example 1

- in a terminal run `python app1.py`
- in a browser go to `localhost:5000`
- in another terminal run `python test1.py`
- in a browser go to `localhost` click the call api button

### example 2

- in a terminal run `python app2.py`
- in a browser go to `localhost:5000`
- in another terminal run `python test2.py`
- in a browser go to `localhost` click the call api button

## further reading

- https://martinfowler.com/articles/microservices.html
- https://flask-restful.readthedocs.io/en/latest/
- alternatives to flask restful (FlaskAPI, Django, GraphQL)
- https://flask-restful.readthedocs.io/en/0.3.6/reqparse.html is deprecated and suggest using https://marshmallow.readthedocs.io/en/3.0/
