(function () {
	"use strict";

	var clients = [];
	var getClients = function () {
		$.ajax({
			url: "https://hh-incident-monitoring-service.herokuapp.com/people", success: function (data) {
				var temppeople = data.people.slice(0);
				var tempclients = clients.slice(0);
				var people = data.people;
				for (var i = 0; i < people.length; i++) {
					var person = people[i];
					for (var j = 0; j < clients.length; j++) {
						var client = clients[j];
						if (person._id == client._id) {
							var tempIncidents = person.events.splice(0);
							for (var k = 0; k < person.events.length; k++) {
								var incident = person.events[k];
								for (var l = 0; l < client.events.length; l++) {
									var event = client.events[l];
									if (incident._id == event._id) {
										tempIncidents.splice(k,1);
									}
								}
							}
							for (var m = 0; m < tempIncidents.length; m++) {
								var incident = tempIncidents[m];
								client.events.push(incident);
								toastr.info("A new incident has been added for " + client.Identity.FNAME + " " + client.Identity.LNAME);
							}
							temppeople.splice(i, 1);
						}
					}
				}
				for (var x = 0; x < temppeople.length; x++) {
					var client = temppeople[x];
					clients.push(client);
					toastr.info(client.Identity.FNAME + " was added to your client list.");
				}
				
				
				
			}, dataType: "json"
		});
	}
	setInterval(function () {
		getClients();
	}, 10000);


	var app = angular
                .module("clientResourceMock",
                ["ngMockE2E"]);

	app.run(function ($httpBackend) {
		 clients = [
			{
				Identity: {
					CITIZEN: "US",
					DOB: "7/31/1969",
					FNAME: "MILES",
					LNAME: "MARTIN",
					MNAME: "ROBERT",
					RACE: "C",
					SEX: "M"
				},
				Sources: [
				"83d150d743734097a4804a81af4dbea9",
				"4f8353f705924e6b90ed6c9e464c29c4",
				"b05b51a063bb4e05b84cc15c29f8848b"
				],
				_id: "361cee526d0a4a1ba24aa4ebfc1e278f",
				_rev: "4-21720edb8c58cbd57538268c9971a3c5",
				events: [
				{
					CASE_ID: "1457",
					DATE: "3/6/2016",
					HEARING_TYPE: "BENCH",
					TIME: "8:00 AM",
					TITLE: "MARTIN, ROB",
					_id: "001caddee7d946cfbd3381f0eae5da16"
				}
				]
			}
			];

		var clientUrl = "api/clients"

		$httpBackend.whenGET(clientUrl).respond(clients);

		var editingRegex = new RegExp(clientUrl + '/[0-9a-z][0-9a-z]*', '')
		$httpBackend.whenGET(editingRegex).respond(function (method, url, data) {
			var client = { "clientId": "0" };
			var parameters = url.split('/');
			var length = parameters.length;
			var id = parameters[length - 1];

			if (id) {
				for (var i = 0; i < clients.length; i++) {
					if (clients[i]._id == id) {
						client = clients[i];
						break;
					}
				}
			}
			return [200, client, {}];
		});


		$httpBackend.whenPOST(clientUrl).respond(function (method, url, data) {
			var client = angular.fromJson(data);

			if (!client._id) {
				client._id = clients[clients.length - 1]._id + "1";
				clients.push(client);
			}
			else {
				for (var i = 0; i < clients.length; i++) {
					if (clients[i]._id == client._id) {
						clients[i] = client;
						break;
					}
				}
			}
			return [200, client, {}];
		});

		$httpBackend.whenGET(/app/).passThrough();

	})
}());