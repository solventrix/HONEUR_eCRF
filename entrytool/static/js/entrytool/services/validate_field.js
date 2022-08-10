angular.module('opal.services').service('ValidateField', function(ValidationRules) {
	return {
		validate:	function(apiName, fieldName, value, instance, episode, patient){
			/*
			* validates for different alertTypes which are either warnings or errors
			*/
			var result = {
				warnings: [],
				errors: []
			}
			var self = this;
			if(ValidationRules[apiName] && ValidationRules[apiName][fieldName]){
				_.each(['warnings', 'errors'], function(alertType){
					if(!ValidationRules[apiName][fieldName][alertType]){
						return;
					}
					_.each(ValidationRules[apiName][fieldName][alertType], function(validator_and_error){
						var validator = validator_and_error[0];
						var error = validator_and_error[1];
						var issue = validator(value, instance, episode, patient);
						if(issue){
							result[alertType].push(error);
						}
					});
				})
			}
			return result;
		}
	}
});
