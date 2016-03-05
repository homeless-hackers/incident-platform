# Homeless Hackers

The Homeless Hackers team is creating an incident monitoring and management platform intended for use by governmental and non-governmental agencies working with at-risk populations, including individuals experiencing homelessness and mental illness.

An incident monitoring service polls various data sources, including courts, jails, prisons, probation and parole records, and reports on criminal and mental health events related to clients of the agencies.

An incident management application subscribes to new events for each client of the agency, and when a new event is received, provides actionable information to the case manager.

## Architecture

* Incident monitoring service
  * Model person and incidents
  * Generate events related to person and incidents

* Incident data services
  * Model data sources

* Incident data scheduler
  * Schedule data service polling by person

* Incident data service
  * Poll a data source by person

* Matching service
  * Generate a confidence interval for matching incidents to monitored persons

* Message broker
  * Receives events from incident monitoring service
  * Publishes events to incident management applications

* Incident management application
  * Subscribe persons to be monitored
  * Subscribe to events per monitored person

## Flow

1. A case manager, using the incident management application, subscribes a client to the incident monitoring service
  * Various personally identifying information is entered with variations, to be used for measuring confidence while matching events
  * Data sources are selected from a list of configured sources
2. The incident data scheduler enters a job to poll each data source for each person (for each variation of name and DOB)
3. The incident data service runs the job as scheduled
4. New incidents are collected from the source, if available
5. A match confidence is calculated for the incident
6. The incident with its match confidence is sent to the incident monitoring service
7. The incident monitoring service publishes an event about the new incident
8. The incident management application receives the event and provides actionable information to the case manager

## Example incidents

* Citation issued
* Hearing or other court appearance scheduled
* Charges filed
* Warrant issued
* Sentence entered
* Jail booking
* Jail release date assigned
* Jail release

## Monitor

The monitor application accepts persons to monitor, and incidents about a person. When any data changes, it publishes an event to the message broker.

### Flow

POST /person : new client
PUT /{id} : update client
DELETE /{id} : unschedule client
POST /{id}/incident : new incident
GET /{id} : retrieve client (includes incidents)

RabbitMQ



