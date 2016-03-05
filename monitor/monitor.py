import amqp
import logging, sys

from flask import Flask, jsonify
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
  return 'Not implemented.'

@app.route('/people', methods=['POST'])
def add_person():
  return 'Not implemented.'

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
