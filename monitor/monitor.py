import amqp
import store
import data
import logging, sys

from flask import Flask, jsonify, request
from flask.ext.cors import CORS

app = Flask(__name__, static_url_path='')
CORS(app)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def hello_world():
  return app.send_static_file('index.html')

@app.route('/rabbit')
def rabbit_test():
  amqp.publish_event(id='personid', event_type='test_event', event='another event message')
  return 'Tried to update Rabbit.'

@app.route('/people', methods=['GET'])
def get_people():
  return jsonify( store.get_people() )

@app.route('/people', methods=['POST'])
def add_person():
  print request.get_json()
  return jsonify( store.store_person( person=data.clean_person( request.get_json() )))

@app.route('/people/<id>', methods=['GET'])
def get_person(id):
  return jsonify( store.get_person(id=id) )

@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
  return jsonify( store.store_person( person=data.clean_person( request.get_json() ), id=id))

@app.route('/people/<id>/incidents', methods=['GET'])
def get_incidents(id):
  return jsonify( store.get_incidents(id=id) )

@app.route('/people/<id>/incidents', methods=['POST'])
def add_incident(id):
  return jsonify( store.store_incident( incident=data.clean_incident( request.get_json() ), id=id))

@app.route('/killkillkill', methods=['GET'])
def killkillkill():
  return store.restart()

if __name__ == '__main__':
  app.run()
