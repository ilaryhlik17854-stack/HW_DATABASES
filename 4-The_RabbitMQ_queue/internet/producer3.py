#!/usr/bin/env python
# coding=utf-8
import pika
credentials = pika.PlainCredentials('admin', 'admin')
parameters = pika.ConnectionParameters('91.214.240.140',
                                   9552,
                                   '/',
                                   credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello Rukhlik IA student Netology!')
connection.close()
