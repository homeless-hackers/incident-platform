import amqp
import store
import data
import logging, sys

from flask import Flask, jsonify, request
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def hello_world():
  return 'This interface is not supported. Go away.'

@app.route('/rabbit')
def rabbit_test():
  amqp.publish_event(id='personid', event_type='test_event', event='another event message')
  return 'Tried to update Rabbit.'

@app.route('/people', methods=['GET'])
def get_people():
  return jsonify( store.get_people() )

@app.route('/people', methods=['POST'])
def add_person():
  return jsonify( store.store_person( person=data.clean_person( request.get_json() )))

@app.route('/people/<id>', methods=['GET'])
def get_person(id):
  return jsonify( store.get_person(id=id) )

@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
  return jsonify( store.store_person( person=data.clean_person( request.get_json() ), id=id))

@app.route('/people/<id>/incidents', methods=['GET'])
def get_incidents(id):
  return 'Not implemented.'

@app.route('/people/<id>/incidents', methods=['POST'])
def add_incident(id):
  return 'Not implemented.'

if __name__ == '__main__':
  app.run()
