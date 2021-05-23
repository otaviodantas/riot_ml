import os
from dotenv import load_dotenv
from flask import Flask
from flask.json import jsonify
from pika import BlockingConnection, ConnectionParameters

load_dotenv()

app = Flask(__name__)
connection = BlockingConnection(ConnectionParameters(os.environ.get('MSG_ADRESS')))
channel = connection.channel()
channel.queue_declare('riot_api')

@app.route('/')
def home():
    return jsonify({'statusCode': 200})


@app.route('/<player_name>')
def start_find_mathcs(player_name: str):
    if player_name is None:
        return  jsonify({
            'statusCode': 405, 
            'message': 'Nome do player é inválido'
            })
    else:
        try:
            channel.basic_publish(
                body=player_name,
                exchange='',
                routing_key='riot_api')
            return jsonify({'statusCode': 200})

        except Exception as e:
            return jsonify({
            'statusCode': 405, 
            'message': e
            })

if __name__ == '__main__':
    app.run()