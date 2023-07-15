


import pika

params = pika.URLParameters('amqps://icmnwovy:ZSZFR3cURlyYM0WXYW2TVvquwgnwhF77@puffin.rmq2.cloudamqp.com/icmnwovy')

connection = pika.BlockingConnection(params)
channel= connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='Hello jan')