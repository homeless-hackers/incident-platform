(function () {
	"use strict";

	angular
        .module("clientManagement")
        .controller("ClientListController",
                ["clientResource",
                ClientListController]);

	function ClientListController(clientResource) {
		var vm = this;

		clientResource.query(function (data) {
			vm.clients = data;
		});


		vm.showImage = false;

		vm.toggleImage = function () {
			vm.showImage = !vm.showImage;
		}
	}
}());
