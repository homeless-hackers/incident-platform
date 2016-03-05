import store

def send_client(file):
  print(store.store_person( person=data.clean_person( open(file, 'rb').read() )))
  print(file)

def send_events(file):
  print(store.store_incident( person=data.clean_incident( open(file, 'rb').read() )))
  print(file)

def wait():
  input("Press Enter to continue...")

def empty_db():
  store.restart()
  print("Database emptied")

def main():
  empty_db()
  wait()
  send_client("mock_data/clients/dan.json")
  wait()
  send_events("mock_data/events/court/dan_court_event1.json")
  wait()
  send_events("mock_data/events/court/dan_court_event2.json")
  send_events("mock_data/events/court/dan_court_event3.json")
  wait()
  send_events("mock_data/events/court/dan_court_event4.json")
  send_events("mock_data/events/court/dan_court_event5.json")
  wait()
  send_client("mock_data/clients/rob.json")
  send_client("mock_data/clients/jen.json")
  send_client("mock_data/clients/bryan.json")
  send_client("mock_data/clients/summer.json")
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
