import os
from dotenv import load_dotenv
from pika import BlockingConnection, ConnectionParameters

load_dotenv()

class DeliveryMan:
    def __init__(self):
        self._connection = BlockingConnection(ConnectionParameters(os.environ.get('MSG_ADRESS')))
        self._channel = self._connection.channel()
        self.queue = None
    
    def publish(self, routing_key, body, exchange=''):
        self._channel.basic_publish(
            routing_key=routing_key,
            body=body,
            exchange=exchange)
        self._close_connection()
        
    def _close_connection(self):
        self._channel.close()

    def _instance_queue(self, queue_name: str) -> None:
        self.queue = self._channel.queue_declare(queue=queue_name)
