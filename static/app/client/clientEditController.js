(function () {
	"use strict";

	angular
		.module("clientManagement")
		.controller("ClientEditController",
		["client",
			"$state",
			"clientService",
			ClientEditController]);

	function ClientEditController(client, $state, clientService) {
		var vm = this;
		vm.client = client;
		vm.opened = false;
		if (vm.client && vm.client.Identity) {
			vm.title = "Edit: " + vm.client.Identity.FNAME + " " + vm.client.Identity.LNAME;
		}
		else {
			vm.title = "New Client";
		}

		vm.submit = function () {
			vm.client.$save(function (data) {
				toastr.success("Save successful");
			});
		}

		vm.cancel = function () {
			$state.go('clientList');
		}
	}
}());
