import requests
import simplejson as json

base = "https://hh-incident-monitoring-service.herokuapp.com/"

def send_client(file):
  data = open(file, 'rb').read().decode(encoding='UTF-8')
  r = requests.post(base + 'people', json = json.loads(data))
  print(r.content)
  response = r.json()
  return response['doc_id']

def send_events(file, id):
  data = open(file, 'rb').read().decode(encoding='UTF-8')
  r = requests.post(base + 'people/' + id + '/incidents', json = json.loads(data))
  print(r.json())

def wait():
  input("Press Enter to continue...")

def empty_db():
  r = requests.get(base + 'killkillkill')
  print("Database emptied")

def main():
  empty_db()
  wait()
  rob = send_client("mock_data/clients/rob.json")
  wait()
  send_events("mock_data/events/jail/rob_jail_event1.json", rob)
  wait()
  send_events("mock_data/events/court/rob_court_event5.json", rob)
  wait()
  send_events("mock_data/events/court/rob_court_event6.json", rob)
  wait()
  send_events("mock_data/events/court/rob_court_event7.json", rob)
  wait()

  bryan = send_client("mock_data/clients/bryan.json")
  send_events("mock_data/events/court/bryan_court_event1.json", bryan)
  send_events("mock_data/events/court/bryan_court_event2.json", bryan)
  send_events("mock_data/events/court/bryan_court_event3.json", bryan)
  send_events("mock_data/events/court/bryan_court_event4.json", bryan)
  send_events("mock_data/events/court/bryan_court_event5.json", bryan)
  send_events("mock_data/events/court/bryan_court_event6.json", bryan)
  send_events("mock_data/events/court/bryan_court_event7.json", bryan)

  dan = send_client("mock_data/clients/dan.json")
  send_events("mock_data/events/court/dan_court_event1.json", dan)
  send_events("mock_data/events/court/dan_court_event2.json", dan)
  send_events("mock_data/events/court/dan_court_event3.json", dan)
  send_events("mock_data/events/court/dan_court_event4.json", dan)
  send_events("mock_data/events/court/dan_court_event5.json", dan)

  jen = send_client("mock_data/clients/jen.json")
  send_events("mock_data/events/court/jen_court_event1.json", jen)
  send_events("mock_data/events/court/jen_court_event2.json", jen)
  send_events("mock_data/events/court/jen_court_event3.json", jen)
  send_events("mock_data/events/court/jen_court_event4.json", jen)
  send_events("mock_data/events/court/jen_court_event5.json", jen)

  summer = send_client("mock_data/clients/summer.json")
  send_events("mock_data/events/court/summer_court_event1.json", summer)
  send_events("mock_data/events/court/summer_court_event2.json", summer)
  send_events("mock_data/events/court/summer_court_event3.json", summer)
  send_events("mock_data/events/court/summer_court_event4.json", summer)
  send_events("mock_data/events/court/summer_court_event5.json", summer)
  send_events("mock_data/events/court/summer_court_event6.json", summer)
  send_events("mock_data/events/court/summer_court_event7.json", summer)
  send_events("mock_data/events/court/summer_court_event8.json", summer)
  send_events("mock_data/events/court/summer_court_event9.json", summer)
  send_events("mock_data/events/court/summer_court_event10.json", summer)
  send_events("mock_data/events/court/summer_court_event11.json", summer)
  send_events("mock_data/events/court/summer_court_event12.json", summer)
  send_events("mock_data/events/court/summer_court_event13.json", summer)
  send_events("mock_data/events/court/summer_court_event14.json", summer)
  send_events("mock_data/events/court/summer_court_event15.json", summer)
  send_events("mock_data/events/court/summer_court_event16.json", summer)

if __name__ == '__main__':
  main()
