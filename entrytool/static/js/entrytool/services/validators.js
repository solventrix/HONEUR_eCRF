angular.module('opal.services').service('Validators', function(EntrytoolHelper, toMomentFilter){
	"use strict";

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



	return {
		validateDateOfDiagnosisAgainstRegimen: function(val, instance, episode, patient){
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
		},
		validateDateOfDiagnosisAgainstResponse: function(val, instance, episode, patient){
			var error = false;
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
		},
		validateDateOfDiagnosisAgainstSCT: function(val, instance, episode, patient, fieldName, modelApiName){
			/*
			* Date of diagnosis must be below all SCT/Regimen/response dates.
			*/
			var error = false;
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
		},
		validateRegimenDateBetween: function (
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
		},
		validateRegimenSurrounds: function (fieldValue, instance, episode, patient) {
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
		},
		validateRegimenToOtherLOTRegimens: function (val, instance, episode, patient){
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
		},
		validateRegimenToResponses: function(val, instance, episode){
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
		},
		validateOnlyOneOpenRegimen: function(val, regimenInstance, episode, patient){
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
		},
		sameOrAfterDiagnosisDate: function(val, instance, episode, patient, fieldName, modelApiName){
			var diagnosis = EntrytoolHelper.getDiagnosis(patient);
			if(!diagnosis){
				return false;
			}
			var diagnosisDate = diagnosis.diag_date;
			if(!val || !diagnosisDate){
				return false;
			}
			if(diagnosisDate.isAfter(val, "d")){
				return true;
			}
		},
		sameOrBeforeDiagnosisDate: function(val, instance, episode, patient, fieldName, modelApiName){
			var diagnosis = EntrytoolHelper.getDiagnosis(patient);
			if(!diagnosis){
				return false;
			}
			var diagnosisDate = diagnosis.diag_date;
			if(!val || !diagnosisDate){
				return false;
			}
			if(diagnosisDate.isBefore(val, "d")){
				return true;
			}
		},
		afterDateOfBirth: function(val, instance, episode, patient, fieldName, modelApiName){
			var dateOfBirth = episode.demographics[0].date_of_birth;
			if(val && dateOfBirth){
				if(dateOfBirth.isAfter(val, "d")){
					return true;
				}
			}
		},
		endDateSameOrAfterRegimenStartDate: function(val, instance){
			var startDate = instance.start_date;
			var endDate = instance.end_date;
			if(endDate && startDate){
				if(toMomentFilter(startDate).isAfter(toMomentFilter(endDate), "d")){
					return true;
				}
			}
		},
		regimenRequiredForMM: function(val, instance){
			if(val){
				return false;
			}
			if(instance.category && instance.category == 'Watch and wait'){
				return false;
			}
			return true;
		},
		regimenRequiredForCLL: function(val, instance){
			if(val){
				return false;
			}
			if(instance.category && instance.category == 'Treatment'){
				return false;
			}
			return true;
		},
		requiredIfSMM: function(val, instance){
			if(val){
				return false;
			}
			if(instance.smm_history !== 'Yes'){
				return false;
			}
			return true
		},
		required: function(val){
			return !val;
		},
		requiredForCategory: function(categoryName){
			return function(val, instance, episode){
				/*
				* If something is only required for a condition
				* e.g. MMDiagnosisDetails are only required
				* if the category is MM
				*/
				if(episode.category_name === categoryName && !val){
					return true;
				}
			}
		},
		lessThan: function(amount){
			return function(val){
				if(_.isNumber(val) && val > amount){
					return true;
				}
			}
		},
		greaterThan: function(amount){
			return function(val){
				if(_.isNumber(val) && val < amount){
					return true;
				}
			}
		},
		maxLength: function(amount){
			return function(val){
				if(_.isNumber(val) && val.length > amount){
					return true;
				}
			}
		},
		noFuture: function(val){
			if(!val){
				return false
			}
			var today = moment();
			if(toMomentFilter(val).isAfter(today, "d")){
				return true;
			}
		},
		validateResponseToRegimens: function(val, instance, episode){
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
		},
	}
});
