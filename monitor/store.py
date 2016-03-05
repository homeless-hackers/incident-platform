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

def store_person(person):
  if person.get('_id'):
    doc_id, doc_rev = update(person)
  else:
    doc_id, doc_rev = create(person)
  return {'doc_id': doc_id, 'doc_rev': doc_rev}

def get_person(id):
  return db[id]

def store_incident(id, incident):
  person = db[id]
  person['events'].append(incident)
  doc_id, doc_rev = update(incident)
  return {'doc_id': doc_id, 'doc_rev': doc_rev}
