import pika, json

params = pika.URLParameters('amqps://usgshgus:EIOpVY4cvh5MM76D9EORpeLLNWvuo0xe@rattlesnake.rmq.cloudamqp.com/usgshgus')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)