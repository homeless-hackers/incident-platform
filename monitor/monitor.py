from amqp import publish_event
from store import store_person, store_incident
from data import clean_person, clean_incident
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
  publish_event(id='personid', event_type='test_event', event='another event message')
  return 'Tried to update Rabbit.'

@app.route('/people', methods=['GET'])
def get_people():
  return 'Not implemented.'

@app.route('/people', methods=['POST'])
def add_person():
  return store_person( clean_person( request.get_json() ))

@app.route('/people/<id>', methods=['GET'])
def get_person(id):
  return 'Not implemented.'

@app.route('/people/<id>', methods=['PUT'])
def update_person(id):
  return 'Not implemented.'

@app.route('/people/<id>/incidents', methods=['GET'])
def get_incidents(id):
  return 'Not implemented.'

@app.route('/people/<id>/incidents', methods=['POST'])
def add_incident(id):
  return 'Not implemented.'

if __name__ == '__main__':
  app.run()
