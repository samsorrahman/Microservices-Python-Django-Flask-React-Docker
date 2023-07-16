

import pika, json, os, django

# the consumer file give error becaue we are using product class but consumer is outside the product project so we add this
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://icmnwovy:ZSZFR3cURlyYM0WXYW2TVvquwgnwhF77@puffin.rmq2.cloudamqp.com/icmnwovy')

connection = pika.BlockingConnection(params)
channel= connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Recieved in admin')
    id= json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)


print('started consuming')

channel.start_consuming()

channel.close()
