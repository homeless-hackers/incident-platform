(function () {
	"use strict";

	angular
        .module("common.services")
        .factory("clientResource",
        ["$resource",
        clientResource]);

	function clientResource($resource) {
		return $resource("api/clients/:clientId");
	}
}());