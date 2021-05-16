from flask import Flask
from flask.json import jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'statusCode': 200})

