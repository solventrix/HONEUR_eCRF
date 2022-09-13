angular.module('opal.services').factory('DataUploadLoader', function($http) {
	return {
		unValidatedPatients: function(){
			return $http.get('/entrytool/v0.1/unvalidated_patients/').then(function(response){
				return response.data;
			});
		},
		patientsWithErrors: function(){
			return $http.get('/entrytool/v0.1/patients_with_errors/').then(function(response){
				return response.data.results;
			});
		}
	}
})
