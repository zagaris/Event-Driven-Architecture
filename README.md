# Event-Driven Microservice Architecture in Python


## How it works

This repository demonstrates an event-driven microservice architecture implementing a Django and a Flask service utilizing RabbitMQ message broker for communication part


## Quick Start

Clone the repo and install the dependencies.

```bash
https://github.com/zagaris/Event-Driven-Architecture.git
cd Event-Driven-Architecture
```
Install the dependencies for the django service and run it
```bash
cd admin
pip install dependencies.txt
docker-compose up --buid
```
Install the dependencies for the flask service and run it

```bash
cd main
pip install dependencies.txt
docker-compose up --buid
```


Change the ```'amqps_key'``` to your amqps key
