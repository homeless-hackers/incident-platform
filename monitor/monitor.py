import amqp
import logging, sys

from flask import Flask
app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/', methods=['GET'])
def hello_world():
  return 'This interface is not supported. Go away.'

@app.route('/rabbit')
def rabbit_test():
  amqp.publish_event('personid', 'test_event', 'my event message')
  return 'Tried to update Rabbit.'

if __name__ == '__main__':
  app.run()
