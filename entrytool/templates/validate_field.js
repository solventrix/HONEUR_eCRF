{% load i18n %}
angular.module('opal.services').service('ValidateField', function(
	toMomentFilter, EntrytoolHelper
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

	var validateRegimenDateBetween = function (
		fieldValue,
		instance,
		episode,
		patient
	) {
		/*
		 * Takes in a field value (a moment), instance (a regimen)
		 * Returns true if the field is between start/end of two
		 * regimen dates and is not the same regimen
		 */
		var error = false;
		if (!fieldValue) {
			return error;
		}
		_.each(patient.episodes, function (episode) {
			_.each(EntrytoolHelper.getEpisodeRegimen(episode), function (r) {
				if (r.id !== instance.id) {
					if (r.start_date && r.end_date) {
						if (fieldValue >= r.start_date && fieldValue <= r.end_date) {
							error = true;
						}
					}
				}
			});
		});

		return error;
	};


	var validateRegimenSurrounds = function (
		fieldValue,
		instance,
		episode,
		patient
	) {
		/*
		 * Make sure that when a regimen date is changed, the regimen does not
		 * now encompass another regimen
		 *
		 * Step 1. Create a regimen A but don't but an end date on it with
		 * start time Monday.
		 * Step 2. Create a regimen B that lasts between Tuesday-Wednesday
		 * Step 3. The add an end date on A of Thursday. It should error.
		 */
		var error = false;
		if (!fieldValue) {
			return;
		}
		_.each(patient.episodes, function (episode) {
			_.each(EntrytoolHelper.getEpisodeRegimen(episode), function (r) {
				if (r.id !== instance.id) {
					if (r.start_date && r.end_date) {
						if (
							instance.start_date < r.start_date &&
							instance.end_date > r.end_date
						) {
							error = true;
						}
					}
				}
			});
		});
		return error;
	};

	var episodeRegimenMinMaxDates = function (episode) {
		return getRegimenMinMaxDate(EntrytoolHelper.getEpisodeRegimen(episode));
	};

	var getRegimenMinMaxDate = function(regimen){
		// returns the first start date and the last end date
		// note end date may be null;
		// pluck the regimen start dates, sort them and return the first
		var episodeMin = _.pluck(regimen, "start_date").sort()[0];
		var episodeMax = null;
		// regimen end date is not required, remove the nulls and
		// make sure any of them are populated
		var episodeMaxVals = _.compact(_.pluck(regimen, "end_date"));
		if (episodeMaxVals.length) {
			episodeMax = _.sortBy(episodeMaxVals).reverse()[0];
		}
		return [episodeMin, episodeMax];
	}

	var validateRegimenToOtherLOTRegimens = function (
		val,
		instance,
		episode,
		patient
	) {
		/*
		 * for an episode's regimens they should not overlap another episodes
		 * regimens
		 */
		// check vs the instance dates as these may have changed.

		if(!val){
			return false;
		}
		var min = toMomentFilter(instance.start_date);
		var max = toMomentFilter(instance.end_date);
		var thisEpisodesRegimen = EntrytoolHelper.getEpisodeRegimen(episode)

		// exclude this regimen's id if it exists
		if(instance.id){
			thisEpisodesRegimen = _.filter(thisEpisodesRegimen, function(r){ return r.id !== instance.id });
		}

		if(thisEpisodesRegimen.length){
			var ourEpisodeMinMax = getRegimenMinMaxDate(thisEpisodesRegimen);
			if(ourEpisodeMinMax[0].isBefore(min, "d")){
				min = ourEpisodeMinMax[0];
			}
			if(!max){
				max = ourEpisodeMinMax[1];
			}
			else if (ourEpisodeMinMax[1] && ourEpisodeMinMax[1].isAfter(max, "d")){
				max = ourEpisodeMinMax[1];
			}
		}

		var error = null;

		_.each(patient.episodes, function (otherEpisode) {
			if (error) {
				return;
			}
			// ignore this episode
			if (episode.id === otherEpisode.id) {
				return;
			}
			if (!EntrytoolHelper.getEpisodeRegimen(otherEpisode).length) {
				return;
			}
			var episodeMinMax = episodeRegimenMinMaxDates(otherEpisode);
			var episodeMin = episodeMinMax[0];
			var episodeMax = episodeMinMax[1];
			// other episode ends before our episode starts
			if(episodeMax && episodeMax.isBefore(min, "d")){
				return;
			}
			// other episode does not have a start but starts before our episode starts
			if(!episodeMax && episodeMin.isBefore(min, "d")){
				return;
			}
			// our episode ends before other episode starts
			if(max && max.isBefore(episodeMin, "d")){
				return;
			}
			// our episode has no end but starts before other episode starts
			if(!max && min.isBefore(episodeMin, "d")){
				return;
			}
			error = true;
		});
		return error;
	};


	var validateRegimenToResponses = function(val, instance, episode){
		/*
		* From the perspective of a regimen, validates that the
		* responses are connected to either other regimens
		* or the regimen in the form.
		*/
	 if(!val || !EntrytoolHelper.getEpisodeResponse(episode).length){
			return;
	 }
		var withinRegimen = false;
		// we may be editing things so ignore version of regimen
		// we are using that is attatched to the episode.
		var regimens = _.reject(EntrytoolHelper.getEpisodeRegimen(episode), {id: instance.id, episode_id: instance.episode_id});
		regimens.push(instance);
		_.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
			if(response.response_date){
				_.each(regimens, function(regimen){
					var within = responseDateWithRegimen(response.response_date, regimen);
					if(within){
						withinRegimen = true;
					}
				});
			}
		});
		if(!withinRegimen){
			return true
		}
	}

	var responseDateWithRegimen = function(fieldValue, regimen){
		/*
		* A response date can be start_date - 30 days or
		* end_date + 30 days and anything in between.
		*/
		var allowedStartDate = moment(regimen.start_date,).add(-30, "d")
		var allowedEndDate = null;
		var withinParams = false;
		if(regimen.end_date){
			allowedEndDate = moment(regimen.end_date).add(30, "d")
			if(fieldValue >= allowedStartDate && fieldValue <= allowedEndDate){
				withinParams = true;
			}
		}
		else{
			if(fieldValue >= allowedStartDate){
				withinParams = true
			}
		}
		return withinParams
	}

	var validateOnlyOneOpenRegimen = function(val, regimenInstance, episode, patient){
		/*
		* There can only be one regimen with no end date, if the user
		* is trying to save a regimen with no end date and there
		* already exists another with no end date, flag it as an error.
		*
		* Note this is a special case of validation as it exists as part of an
		* ng-required not ng-change like the rest of the validation.
		*
		* It returns false if there is no error or true if there is an error
		*/

		// if there is a val then there is an end date for this
		// regimen and we don't need to check the other episodes
		if(val){
			return
		}
		var otherOpenEndRegimenExists = false
		_.each(patient.episodes, function(episode){
			var regimen = EntrytoolHelper.getEpisodeRegimen(episode);
			var regimenWithNoEndDate = _.filter(regimen, function(r){
				if(!r.end_date){
					// ignore the current instance
					if(regimenInstance.id && regimenInstance.id === r.id){
						return false
					}
					return true
				}
			});
			if(regimenWithNoEndDate.length){
				otherOpenEndRegimenExists = true
			}
		});
		return otherOpenEndRegimenExists;
	}

	var sameOrAfterDiagnosisDate = function(val, instance, episode, patient, fieldName, modelApiName){
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

	var endDateSameOrAfterRegimenStartDate = function(val, instance){
		var startDate = instance.start_date;
		var endDate = instance.end_date;
		if(endDate && startDate){
			if(toMomentFilter(startDate).isAfter(toMomentFilter(endDate), "d")){
				return true;
			}
		}
	}

	var regimenRequired = function(val, instance){
		if(val){
			return false;
		}
		if(instance.category && instance.category == 'Watch and wait'){
			return false;
		}
		return true;
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
			if(_.isNumber(val) && val < amount){
				return true;
			}
		}
	}

	var maxLength = function(amount){
		return function(val){
			if(_.isNumber(val) && val.length > amount){
				return true;
			}
		}
	}

	var noFuture = function(val){
		if(!val){
			return false
		}
		var today = moment();
		if(toMomentFilter(val).isAfter(today, "d")){
			return true;
		}
	}

	var validateResponseToRegimens = function(val, instance, episode){
		/*
		* From the perspective of a response_date, validates that there
		* is a regimen related to it.
		*/
		if(!val){
			return false;
		}
		var withinRegimen = false;
		_.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
			var within = responseDateWithRegimen(val, regimen);
			if(within){
				withinRegimen = true;
			}
		});
		if(!withinRegimen){
			return true;
		}
	}

	var requiredIfCategoryIsTreatment = function(val, instance){
		if(!val && instance.category == 'Treatment'){
			return true
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

		// general validators
		demographics: {
			hospital_number: {
				errors: [
					[required, "{% trans "External identifier is required" %}"],
					[maxLength(255), "{% trans "Maximum length is 255" %}"]
				]
			},
			sex: {
				errors: [
					[required, "{% trans "Sex is required" %}"]
				]
			}
		},
		patient_status: {
			death_date: {
				errors: [
					[afterDateOfBirth,  "{% trans "Date of death is before the date of birth" %}"]
				]
			}
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
			},
		},

		// MM validators
		mm_regimen: {
			hospital: {
				errors: [
					[required, "{% trans "Hospital is required" %}"]
				]
			},
			category: {
				errors: [
					[required, "{% trans "Category is required" %}"]
				]
			},
			regimen: {
				errors: [
					[regimenRequired, "{% trans "Regimen is required" %}"]
				]
			},
			start_date: {
				errors: [
					[required, "{% trans "Start date is required" %}"],
					[sameOrAfterDiagnosisDate, "{% trans "Regimen start date must be after the date of diagnosis" %}"],
					[validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[sameOrAfterDiagnosisDate, "{% trans "Regimen start date must be after the date of diagnosis" %}"],
					[validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
					[validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
		},
		mm_response: {
			progression_date: {
				errors: [
					[sameOrAfterDiagnosisDate,  "{% trans "The progression should be after the date of diagnosis" %}"],
					[noFuture, "{% trans "The progression date is in the future" %}"]
				],
				warnings: [
					[validateResponseToRegimens,  "{% trans "No regimen is connected to this response" %}"]
				]
			},
			response_date: {
				errors: [
					[sameOrAfterDiagnosisDate,  "{% trans "The progression should be after the date of diagnosis" %}"],
					[required,  "{% trans "The response date is required" %}"],
					[noFuture, "{% trans "The response date is in the future" %}"]
				],
				warnings: [
					[validateResponseToRegimens,  "{% trans "No regimen is connected to this response" %}"]
				]
			},
		},
		sct: {
			sct_date: {
				errors: [
					[sameOrAfterDiagnosisDate,  "{% trans "The SCT should be after the date of diagnosis" %}"],
					[noFuture, "{% trans "The date of SCT is in the future" %}"]
				]
			}
		},
		lab_test: {
			date: {
				errors: [
					[afterDateOfBirth,  "{% trans "Lab test date must be after the patient's birth date" %}"],
					[required, "{% trans "The date is required" %}"],
				]
			},
			hospital: {
				errors: [
					[required, "{% trans "The hospital is required" %}"],
				]
			},
			creatinine: {
				errors: [
					[lessThan(20), "{% trans "Creatinine is too high" %}"],
					[greaterThan(0.5), "{% trans "Creatinine is too low" %}"],
				]
			},
			mprotein_24h: {
				errors: [
					[lessThan(0), "{% trans "Mprotein in 24 hour is too high" %}"],
					[greaterThan(1000), "{% trans "Mprotein in 24 hour is too low" %}"],
				]
			},
			calcium: {
				errors: [
					[lessThan(6.5), "{% trans "Calcium is too high" %}"],
					[greaterThan(25), "{% trans "Calcium is too low" %}"],
				]
			},
			beta2m: {
				errors: [
					[lessThan(0), "{% trans "Beta2m is too high" %}"],
					[greaterThan(1000), "{% trans "Beta2m is too low" %}"],
				]
			}
		},
		mm_cytogenetics: {
			date: {
				errors: [
					[required, "{% trans "The date is required" %}"],
				]
			},
			hospital: {
				errors: [
					[required, "{% trans "The hospital is required" %}"],
				]
			}
		},
		// CLL validators
		cll_diagnosis_details: {
			diag_date: {
				errors: [
					[validateDateOfDiagnosis, "{% trans "Date of diagnosis is greater than a regimen start date" %}"],
					[required, "{% trans "Date of diagnosis is required" %}"],
					[afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
				]
			},
			binet_stage: {
				errors: [
					[required, "{% trans "Binet stage is required" %}"]
				]
			}
		},
		cll_regimen: {
			regimen: {
				errors: [
					[requiredIfCategoryIsTreatment, "{% trans "Regimen is required" %}"]
				]
			},
			start_date: {
				errors: [
					[required, "{% trans "Start date is required" %}"],
					[sameOrAfterDiagnosisDate, "{% trans "Regimen start date must be after the date of diagnosis" %}"],
					[validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[sameOrAfterDiagnosisDate, "{% trans "Regimen start date must be after the date of diagnosis" %}"],
					[validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
					[validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
		},
		binet_stage: {

		}


	}
});
