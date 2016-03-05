import requests
import simplejson as json

base = "https://hh-incident-monitoring-service.herokuapp.com/"

def send_client(file):
  data = open(file, 'rb').read()
  print(data)
  r = requests.post(base + 'people', data = data)
  print(r.content)
  #response = r.json()
  #return response['doc_id']

  print(file)

def send_events(file, id):
  data = open(file, 'rb').read()
  r = requests.post(base + 'people/' + id + '/incidents', data = data)
  print(r.json())

def wait():
  input("Press Enter to continue...")

def empty_db():
  r = requests.get(base + 'killkillkill')
  print("Database emptied")

def main():
  empty_db()
  wait()
  dan = send_client("mock_data/clients/dan.json")
  wait()
  send_events("mock_data/events/court/dan_court_event1.json")
  wait()
  send_events("mock_data/events/court/dan_court_event2.json")
  send_events("mock_data/events/court/dan_court_event3.json")
  wait()
  send_events("mock_data/events/court/dan_court_event4.json")
  send_events("mock_data/events/court/dan_court_event5.json")
  wait()
  rob = send_client("mock_data/clients/rob.json")
  jen = send_client("mock_data/clients/jen.json")
  bryan = send_client("mock_data/clients/bryan.json")
  summer = send_client("mock_data/clients/summer.json")
  wait()
  send_events("mock_data/events/court/rob_court_event1.json")
  send_events("mock_data/events/court/rob_court_event2.json")
  send_events("mock_data/events/court/rob_court_event3.json")
  send_events("mock_data/events/court/rob_court_event4.json")
  send_events("mock_data/events/court/rob_court_event5.json")
  send_events("mock_data/events/court/rob_court_event6.json")
  send_events("mock_data/events/court/rob_court_event7.json")
  send_events("mock_data/events/court/rob_court_event8.json")
  wait()
  send_events("mock_data/events/court/jen_court_event1.json")
  send_events("mock_data/events/court/jen_court_event2.json")
  send_events("mock_data/events/court/jen_court_event3.json")
  send_events("mock_data/events/court/jen_court_event4.json")
  send_events("mock_data/events/court/jen_court_event5.json")


if __name__ == '__main__':
  main()
