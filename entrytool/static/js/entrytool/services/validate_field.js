angular.module('opal.services').service('ValidateField', function(
	EntrytoolHelper, $injector
) {
	"use strict";

	var VALDATION_ERRORS = $injector.get('VALDATOR_ERRORS');


	var validateDateOfDiagnosis = function(val, instance, episode, patient){
		/*
		* Date of diagnosis must be below all SCT/Regimen/response dates.
		*/
		var error_msg = null;
		_.each(patient.episodes, function(episode){
			_.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
				if(regimen.start_date < val){
					error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_REGIMEN_START
				}
			});
		})
		if(error_msg){
			return error_msg
		}
		var error_msg = null;
		_.each(patient.episodes, function(episode){
			_.each(episode.sct, function(sct){
				if(sct.sct_date < val){
					error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_SCT;
				}
			});
		})
		if(error_msg){
			return error_msg
		}

		var error_msg = null;
		_.each(patient.episodes, function(episode){
			_.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
				if(response.response_date < val){
					error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_RESPONSE;
				}
			});
		})
		if(error_msg){
			return error_msg
		}
	};

	return {
		validate: function(apiName, fieldName, value, instance, episode, patient){
			var errors = [];
			if(this[apiName] && this[apiName][fieldName]){
				_.each(this[apiName][fieldName].errors, function(validator){
					var result = validator(value, instance, episode, patient);
					if(result){
						errors.push(result)
					}
				});
			}
			return errors;
		},
		mm_diagnosis_details: {
			diag_date: {
				errors: [validateDateOfDiagnosis]
			}
		},
		cll_diagnosis_details: {
			diag_date: {
				errors: [validateDateOfDiagnosis]
			}
		}
	}
});
