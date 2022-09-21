angular.module('opal.services').service('ValidateField', function(ValidationRules) {
	return {
		validate:	function(apiName, fieldName, value, instance, episode, patient, schema, lookuplists){
			/*
			* validates for different alertTypes which are either warnings or errors
			*/
			var result = {
				warnings: [],
				errors: []
			}
			if(ValidationRules[apiName] && ValidationRules[apiName][fieldName]){
				_.each(ValidationRules[apiName][fieldName], function(alertFunctions, alertType){
					_.each(alertFunctions, function(validator_and_error){
						// only return the first warning/error
						if(result[alertType].length){
							return;
						}
						var validator = validator_and_error[0];
						var error = validator_and_error[1];
						var isValid = validator(value, instance, episode, patient, apiName, fieldName, schema, lookuplists);
						if(!isValid){
							result[alertType].push(error);
						}
					});
				})
			}
			return result;
		}
	}
});
