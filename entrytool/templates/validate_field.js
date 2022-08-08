{% load i18n %}
angular.module('opal.services').service('ValidateField', function(
	EntrytoolHelper
) {
	"use strict";

	var validateDateOfDiagnosis = function(val, instance, episode, patient, fieldName, modelApiName){
		/*
		* Date of diagnosis must be below all SCT/Regimen/response dates.
		*/
		var error = false;
		_.each(patient.episodes, function(episode){
			_.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
				if(regimen.start_date < val){
					error = true;
				}
			});
		})
		if(error){
			return error
		}
		_.each(patient.episodes, function(episode){
			_.each(episode.sct, function(sct){
				if(sct.sct_date < val){
					error = true;
				}
			});
		})
		if(error){
			return error
		}

		var error = null;
		_.each(patient.episodes, function(episode){
			_.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
				if(response.response_date < val){
					error = true;
				}
			});
		})
		if(error){
			return error
		}
	}

	var afterDiagnosisDate = function(val, instance, episode, patient, fieldName, modelApiName){
		var diagnosisDate = EntrytoolHelper.getDiagnosis(patient).diag_date;
		if(!val || !diagnosisDate){
			return false;
		}
		if(diagnosisDate.isAfter(val, "d")){
			return true;
		}
	}

	var afterDateOfBirth = function(val, instance, episode, patient, fieldName, modelApiName){
		var dateOfBirth = episode.demographics[0].date_of_birth;
		if(val && dateOfBirth){
			if(dateOfBirth.isAfter(val, "d")){
				return true;
			}
		}
	}

	var required = function(val){
		return !val;
	}

	var lessThan = function(amount){
		return function(val){
			if(val && val > amount){
				return true;
			}
		}
	}

	var greaterThan = function(amount){
		return function(val){
			if(val < amount){
				return true;
			}
		}
	}

	return {
		validate: function(apiName, fieldName, value, instance, episode, patient){
			/*
			* validates for different alertTypes which are either warnings or errors
			*/
			var result = {
				warnings: [],
				errors: []
			}
			var self = this;
			if(self[apiName] && self[apiName][fieldName]){
				_.each(['warnings', 'errors'], function(alertType){
					if(!self[apiName][fieldName][alertType]){
						return;
					}
					_.each(self[apiName][fieldName][alertType], function(validator_and_error){
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
		},
		mm_diagnosis_details: {
			diag_date: {
				errors: [
					[validateDateOfDiagnosis, "{% trans "Date of diagnosis is greater than a regimen start date" %}"],
					[required, "{% trans "Date of diagnosis is required" %}"],
					[afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
				]
			},
			iss_stage: {
				errors: [
					[required, "{% trans "ISS stage is required" %}"],
				]
			}
		},
		mm_regimen: {
			start_date: {
				errors: [
					[afterDiagnosisDate, "Regimen start date must be after the date of diagnosis"]
				]
			}
		},
		cll_diagnosis_details: {
			diag_date: {
				errors: [
					[validateDateOfDiagnosis, "{% trans "Date of diagnosis is greater than a regimen start date" %}"],
				]
			}
		},
		lab_test: {
			creatinine: {
				errors: [
					[lessThan(20), "{% trans "Creatinine is too high" %}"],
					[greaterThan(0.5), "{% trans "Creatinine is too low" %}"],
				]
			}
		}
	}
});
