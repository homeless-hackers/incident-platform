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
							if (client.events) {
								var tempIncidents = person.events.slice(0);
								for (var k = 0; k < client.events.length; k++) {
									var incident = client.events[k];
									for (var l = 0; l < person.events.length; l++) {
										var event = person.events[l];
										if (incident._id == event._id) {

											var p = tempIncidents.indexOf(incident);
											tempIncidents.splice(p, 1);
										}
									}
								}
								for (var m = 0; m < tempIncidents.length; m++) {
									var incident = tempIncidents[m];
									client.events.push(incident);
									toastr.info("An new incident has been added for " + client.FNAME + " " + client.LNAME);
								}
							}
							else {
								client.events = [];
							}
							var q = temppeople.indexOf(client);
							temppeople.splice(q, 1);
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
	}, 2000);
	getClients();


	var app = angular
                .module("clientResourceMock",
                ["ngMockE2E"]);

	app.run(function ($httpBackend) {
		 clients = [];

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