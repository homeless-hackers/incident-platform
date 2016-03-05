import couchdb
from uuid import uuid4
import os

params = {
  'url': os.environ.get('COUCH_URL'),
  'db': os.environ.get('COUCH_DB'),
  'username': os.environ.get('COUCH_USERNAME'),
  'password': os.environ.get('COUCH_PASSWORD')
}
couch = couchdb.Server(params['url'])
couch.resource.credentials = (params['username'], params['password'])
db = couch[params['db']]

def create(document):
  document['_id'] = uuid4().hex
  return db.save(document)

def update(document):
  doc = db[document['_id']]
  document['_rev'] = doc['_rev']
  return db.save(document)

def store_person(person, id=False):
  if id:
    person['_id'] = id
    doc_id, doc_rev = update(person)
  else:
    doc_id, doc_rev = create(person)
  return {'doc_id': doc_id, 'doc_rev': doc_rev}

def get_people():
  return {'people': [db[id] for id in db]}

def get_person(id):
  return db[id]

def store_incident(incident, id):
  person = db[id]
  events = person.get('events', [])
  incident['_id'] = uuid4().hex
  events.append(incident)
  person['events'] = events
  doc_id, doc_rev = update(person)
  return {'doc_id': doc_id, 'doc_rev': doc_rev}

def get_incidents(id):
  return {'incidents': db[id]['events'] }
