import pika, os
from urlparse import urlparse

url_str = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost//')
url = urlparse(url_str)
params = pika.ConnectionParameters(
  host=url.hostname,
  virtual_host=url.path[1:],
  credentials=pika.PlainCredentials(url.username, url.password))

def connect_to_rabbit(params):
  return pika.BlockingConnection(params)

def publish_event(id, event_type, event):
  connection = connectToRabbit(params)
  channel = connection.channel()
  channel.exchange_declare(exchange='events') 
  channel.basic_publish(exchange='events', routing_key=id + "." + event_type, body=event)
  connection.close()
