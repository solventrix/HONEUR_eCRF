angular.module('opal.services').factory('DataUploadLoader', function($http) {
	return {
		unValidatedPatients: function(){
			return $http.get('/entrytool/v0.1/unvalidated_patients/').then(function(response){
				return response.data;
			});
		},
		patientsWithErrors: function(page){
			var url = '/entrytool/v0.1/patients_with_errors/';

			if(page){
				url = url + "?" + $.param({page: page});
			}
			return $http.get(url).then(function(response){
				return response.data;
			});
		}
	}
})
