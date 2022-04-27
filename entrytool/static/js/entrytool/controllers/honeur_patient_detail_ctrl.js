angular.module('opal.controllers').controller("HoneurPatientDetailCtrl", function($scope, $rootScope){
	this.editItem = function(item_name, item, episode){
		return episode.recordEditor.editItem(item_name, item).then(function(){
			$rootScope.patientValidator.clean();
		});
	}
});
