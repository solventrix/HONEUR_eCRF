angular.module('opal.services').factory('ValidatePatient', function(
	$q, EntrytoolHelper, $injector
) {
	"use strict";

	var _validatePatient = function(patient, deferred){
		deferred.resolve(['some error']);
	}
	return {
		validatePatient: function(patient){
			var deferred = $q.defer();
			_validatePatient(patient, deferred);
			return deferred.promise;
		}
	}
});
