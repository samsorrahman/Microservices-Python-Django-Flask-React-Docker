


import pika

params = pika.URLParameters('amqps://icmnwovy:ZSZFR3cURlyYM0WXYW2TVvquwgnwhF77@puffin.rmq2.cloudamqp.com/icmnwovy')

connection = pika.BlockingConnection(params)
channel= connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback)


print('started consuming')

channel.start_consuming()

channel.close()
