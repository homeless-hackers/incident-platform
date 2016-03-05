(function () {
	"use strict";
	var app = angular.module("clientManagement",
                            ["common.services",
                             "ui.router",
							 "ui.mask",
							 "ui.bootstrap",
                            "clientResourceMock"]);
	app.config(["$provide", function ($provide) {
		$provide.decorator("$exceptionHandler",
			["$delegate",
				function ($delegate) {
					return function (exception, cause) {
						exception.message = "Error: " + exception.message;
						$delegate(exception, cause);
						alert(exception.message);
					}
				}
			])
	}]);
	app.config(["$stateProvider",
		"$urlRouterProvider",
        function ($stateProvider, $urlRouterProvider) {
        	$urlRouterProvider.otherwise("/");
        	$stateProvider
				.state("home", {
					url: "/",
					templateUrl: "app/welcomeView.html"
				})
				.state("clientList", {
					url: "/client",
					templateUrl: "app/client/clientListView.html",
					controller: "ClientListController as vm"
				})
				.state("clientEdit", {
					abstract: true,
					url: "/client/edit/:clientId",
					templateUrl: "app/client/clientEditView.html",
					controller: "ClientEditController as vm",
					resolve: {
						clientResource: "clientResource",
						client: function (clientResource, $stateParams) {
							var clientId = $stateParams.clientId;
							return clientResource.get({ clientId: clientId }).$promise;
						}
					}
				})
				.state("clientEdit.info", {
					url: "/info",
					templateUrl: "app/client/clientEditInfoView.html"
				})
				.state("clientEdit.incidents", {
					url: "/incidents",
					templateUrl: "app/client/clientEditIncidentsView.html"
				})
        }]
	);
}());