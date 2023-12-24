#!/usr/bin/env python
import pika, sys, os

def handle_message(ch, method, properties, body):
    print(f" [x] Received {body}")
    send_message(ch, method, properties, body)

def send_message(ch, method, properties, body):
  response = "Acknowledged: " + str(body)
  ch.basic_publish(exchange='', routing_key=properties.reply_to, body=response)


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', on_message_callback=handle_message, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
