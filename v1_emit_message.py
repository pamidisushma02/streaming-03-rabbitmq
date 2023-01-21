"""
    This program sends a message to a queue on the RabbitMQ server.

<<<<<<< HEAD
    Author: Denise Case
    Date: January 14, 2023
=======
    Author: Sushma Pamidi
    Date: January 20, 2023
>>>>>>> 42e8cb6 (Module 3)

"""

# add imports at the beginning of the file
import pika

<<<<<<< HEAD
=======
message = "Hello World11"
>>>>>>> 42e8cb6 (Module 3)
# create a blocking connection to the RabbitMQ server
conn = pika.BlockingConnection(pika.ConnectionParameters("LOCALHOST"))
# use the connection to create a communication channel
ch = conn.channel()
# use the channel to declare a queue
ch.queue_declare(queue="hello")
# use the channel to publish a message to the queue
<<<<<<< HEAD
ch.basic_publish(exchange="", routing_key="hello", body="Hello World!")
# print a message to the console for the user
print(" [x] Sent 'Hello World!'")
=======
ch.basic_publish(exchange="", routing_key="hello", body=message)
# print a message to the console for the user
print(f" [x] Sent {message}")
>>>>>>> 42e8cb6 (Module 3)
# close the connection to the server
conn.close()
