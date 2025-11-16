#!/usr/bin/env python
# coding=utf-8
import pika
credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('91.214.240.140',
                                   9555,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(on_message_callback=callback, queue='hello', auto_ack=True)
channel.start_consuming()
