import pika

class SendService:
        def send_message(self, message):
                connection = pika.BlockingConnection(pika.ConnectionParameters('messagequeue'))
                channel = connection.channel()

                channel.queue_declare(queue='hello')

                channel.basic_publish(exchange='',
                                routing_key='hello',
                                body=message)