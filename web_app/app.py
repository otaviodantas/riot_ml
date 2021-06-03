from .send import DeliveryMan
from flask import Flask
from flask.json import jsonify


app = Flask(__name__)
rabbitmq_delivery = DeliveryMan()


@app.route('/')
def home():
    return jsonify({'statusCode': 200})

@app.route('/matchs/<player_name>')
def start_find_mathcs(player_name: str):
    if player_name is None:
        return  jsonify({
            'statusCode': 405, 
            'message': 'Nome do player é inválido'
            })
    else:
        try:
            rabbitmq_delivery.publish(routing_key='riot_api', body=player_name)
            return jsonify({'statusCode': 200})

        except Exception as e:
            return jsonify({
            'statusCode': 405, 
            'message': e
            })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')