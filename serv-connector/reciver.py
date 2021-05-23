import os
from handle_env import load
from pika import BlockingConnection, ConnectionParameters

load()

def main():
    connection = BlockingConnection(ConnectionParameters(os.environ.get('MSG_ADRESS')))
    channel = connection.channel()

    def callback(ch, method, properties, body):
        #TODO: implementar consumo da menssagem
        ...
    
    channel.basic_consume(
        queue='InputDate', 
        on_message_callback=callback,
        auto_ack=True)

    print(' [*] Esperando messagem')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except:
        ...
 