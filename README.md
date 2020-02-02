# Currency Converter Service

CCS it's a simple, lightweight currency conventer service developed in python. You can convert amount of one currency to another with REST API requests. The rates based on PLN currency from api.nbp.pl.

# QuickStart:
This quickstart will show you how to install dependencies and run application locally.

## System Dependencies:
    python3.x and pip3.x, python3-devel, python3-setuptools, build-essential, gcc
    port 5000:5000
    port 80:80
    
#### At first you need to clone this repository by:
    git clone 

#### Create virtualenv with your version of python3:
    virtualenv --python=python3.7 .venv
    source .venv/bin/activate
    
#### Install python3 dependencies:
    pip3 install -r requirements.txt
    
# You can run application as:

#### Development version:
    python3 server.py
    or
    uwsgi --ini CCS.ini
* this version runs at 5000 port

#### Docker version:
    docker build -t ccs .
    docker run --network=host -d -ti ccs
* this version run at 5000 port

#### With dockerized nginx:
in nginx/ direcory
   
    docker build -t ccsnginx .
    docker run --network=host -d -ti ccsnginx
* this version run with nginx at 80 port 

#### Docker-compose version:
    docker-compose build
    docker-compose up
* this version run with nginx at 80 port

#### For test you can make request like:
    curl -v -X POST -d '{"amount":100, "currency1": "USD", "currency2": "PLN"}' -H "Content-Type: application/json" http://0.0.0.0:<running-port>/convert
#### Response:
    {"currency1": "USD", "currency2": "PLN", "amount": 100, "value2": 389.99}


# How to use ?
Basically you should create json with attributes:

* **currency1** - It's "from" currency code
* **currency2** - It's "to" currency code
* **amount** - It's value that would be convert

#### Example: 

    {"amount":100, "currency1": "USD", "currency2": "PLN"}

You will POST this as a data to "/convert" endpoint and recive converted value at response in attribute "value2".
    
    {"currency1": "USD", "currency2": "PLN", "amount": 100, "value2": 389.99}


## Run Unit tests
In main project directory, with activated virtualenv, you should execute:

    py.test -s --cov . --cov-report=term-missing --cov-fail-under=100 --no-cov-on-fail 

## TODO
* Add logging to file, volumes

# Enjoy

