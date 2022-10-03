angular.module('opal.services').service('Validators', function(EntrytoolHelper, toMomentFilter){
	"use strict";
	/*
	* The naming convention of a Validator is to say what the data
	* should look like.
	*
	* A validator is a function that takes
	*    * The field value
	*    * The subrecord instance (e.g. demographics)
	*    * The episode the subrecord is connected to
	*   * The patient the episode is conntected to
	*
	* It returns false if the validator should fail.
	*/

	var episodeRegimenMinMaxDates = function (episode) {
		return getRegimenMinMaxDate(EntrytoolHelper.getEpisodeRegimen(episode));
	};

	var getRegimenMinMaxDate = function(regimen){
		// returns the first start date and the last end date
		// note end date may be null;
		// pluck the regimen start dates, sort them and return the first
		var startDates = _.compact(_.pluck(regimen, "start_date"));
		var endDates = _.compact(_.pluck(regimen, "end_date"))
		var dates = startDates.concat(endDates);
		if(dates.length){
			return [dates[0], _.last(dates)]
		}
		else{
			return [null, null];
		}
	}

	var responseDateWithRegimen = function(fieldValue, regimen){
		/*
		* A response date can be start_date - 30 days or
		* end_date + 30 days and anything in between.
		*/
		if(!regimen.start_date && !regimen.end_date){
			return false;
		}
		var startDate = regimen.start_date;
		if(!startDate){
			startDate = regimen.end_date;
		}
		var allowedStartDate = moment(startDate).add(-30, "d")
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

	var required = function(someVal){
		/*
		* Returns true if someVal is not null/undefined/an empty string
		*/
		if(_.isNull(someVal)){
			return false;
		}
		if(_.isUndefined(someVal)){
			return false;
		}
		if(_.isString(someVal) && !someVal.length){
			return false;
		}
		return true
	}

	return {
		dateOfDiagnosisAgainstRegimen: function(val, instance, episode, patient){
			/*
			* Returns true if there is a regimen start date before the date of diagnosis
			*/
			if(!val){
				return true;
			}
			var error = true;
			_.each(patient.episodes, function(episode){
				_.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
					var regimenDate = regimen.start_date || regimen.end_date;
					if(regimenDate && regimenDate.isBefore(toMomentFilter(val), "d")){
						error = false;
					}
				});
			})
			return error;
		},
		dateOfDiagnosisAgainstResponse: function(val, instance, episode, patient){
			/*
			* Returns true if there is a response date the date of diagnosis
			*/
			if(!val){
				return true;
			}
			var error = true;
			_.each(patient.episodes, function(episode){
				_.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
					if(!response.response_date){
						return;
					}
					if(response.response_date.isBefore(toMomentFilter(val), "d")){
						error = false;
					}
				});
			})
			return error;
		},
		dateOfDiagnosisAgainstSCT: function(val, instance, episode, patient, fieldName, modelApiName){
			/*
			* Date of diagnosis must be below all SCT/Regimen/response dates.
			*/
			if(!val){
				return true;
			}
			var error = true;
			_.each(patient.episodes, function(episode){
				_.each(episode.sct, function(sct){
					if(sct.sct_date && sct.sct_date.isBefore(toMomentFilter(val), "d")){
						error = false;
					}
				});
			})
			return error;
		},
		notBetweenRegimenDates: function (
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
			var error = true;
			if (!fieldValue) {
				return error;
			}
			var val = toMomentFilter(fieldValue);
			_.each(patient.episodes, function (episode) {
				_.each(EntrytoolHelper.getEpisodeRegimen(episode), function (r) {
					if (r.id !== instance.id) {
						if(r.start_date && r.end_date) {
							if(val.isSame(r.start_date, "d")){
								error = false;
							}
							if(val.isSame(r.end_date, "d")){
								error = false;
							}
							if(val.isAfter(r.start_date, "d") && val.isBefore(r.end_date, "d")){
								error = false
							}
						}
					}
				});
			});

			return error;
		},
		regimenToOtherLOTRegimens: function (val, instance, episode, patient){
			/*
			 * If LOT 1 has a regimen starts 1 Jan - > 1 Feb, and 1 Sep -> 1 Oct
			 * LOT 2 cannot have a regimen 1 Mar -> 1 Apr
			 */
			if(!val){
				return true;
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

				if(!min && ourEpisodeMinMax[0]){
					min = ourEpisodeMinMax[0];
				}
				else if(ourEpisodeMinMax[0] && ourEpisodeMinMax[0].isBefore(min, "d")){
					min = ourEpisodeMinMax[0];
				}

				if(!max){
					max = ourEpisodeMinMax[1];
				}
				else if (ourEpisodeMinMax[1] && ourEpisodeMinMax[1].isAfter(max, "d")){
					max = ourEpisodeMinMax[1];
				}

				if(!min){
					min = max;
				}
				if(!max){
					max = min;
				}
				if(!min && !max){
					return true
				}
			}

			var error = false;

			_.each(patient.episodes, function (otherEpisode) {
				if (error) {
					return;
				}
				// ignore this episode
				if (episode.id === otherEpisode.id) {
					return;
				}

				var episodeMinMax = episodeRegimenMinMaxDates(otherEpisode);
				var episodeMin = episodeMinMax[0];
				var episodeMax = episodeMinMax[1];
				if(!episodeMin && !episodeMax){
					// the other episode has no regimen
					return;
				}

				if(!episodeMin){
					episodeMin = episodeMax;
				}

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
			return !error;
		},
		regimenToResponses: function(val, instance, episode){
			/*
			* From the perspective of a regimen, validates that the
			* responses are connected to either other regimens
			* or the regimen in the form.
			*/
		 if(!val){
				return true;
		 }

		 var responses = EntrytoolHelper.getEpisodeResponse(episode);

		 if(!responses.length){
			return true;
		 }
			var withinRegimen = false;
			_.each(responses, function(response){
				if(response.response_date){
					var within = responseDateWithRegimen(response.response_date, instance);
					if(within){
						withinRegimen = true;
					}
				}
			});

			return withinRegimen;
		},
		onlyOneOpenRegimen: function(val, regimenInstance, episode, patient){
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
				return true;
			}
			var otherOpenEndRegimenExists = true
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
					otherOpenEndRegimenExists = false
				}
			});
			return otherOpenEndRegimenExists;
		},
		sameOrAfterDiagnosisDate: function(val, instance, episode, patient, fieldName, modelApiName){
			var diagnosis = EntrytoolHelper.getDiagnosis(patient);
			if(!diagnosis){
				return true;
			}
			var diagnosisDate = diagnosis.diag_date;
			if(!val || !diagnosisDate){
				return true;
			}
			if(diagnosisDate.isAfter(val, "d")){
				return false;
			}
			return true;
		},
		sameOrBeforeDiagnosisDate: function(val, instance, episode, patient, fieldName, modelApiName){
			var diagnosis = EntrytoolHelper.getDiagnosis(patient);
			if(!diagnosis){
				return true;
			}
			var diagnosisDate = diagnosis.diag_date;
			if(!val || !diagnosisDate){
				return true;
			}
			if(diagnosisDate.isBefore(val, "d")){
				return false;
			}
			return true;
		},
		afterDateOfBirth: function(val, instance, episode, patient, fieldName, modelApiName){
			var dateOfBirth = episode.demographics[0].date_of_birth;
			if(val && dateOfBirth){
				if(dateOfBirth.isAfter(val, "d")){
					return false;
				}
			}
			return true;
		},
		endDateSameOrAfterRegimenStartDate: function(val, instance){
			var startDate = instance.start_date;
			var endDate = instance.end_date;
			if(endDate && startDate){
				if(toMomentFilter(startDate).isAfter(toMomentFilter(endDate), "d")){
					return false;
				}
			}
			return true;
		},
		requiredIfSMM: function(val, instance){
			if(instance.smm_history !== 'Yes'){
				return true;
			}
			return required(val);
		},
		required: function(val){
			return required(val);
		},
		CLLRegimenRequired: function(val, instance){
			/*
			* Regimen is not required if the instance category is not treatment
			*/
			if(instance.category !== 'Treatment'){
				return true;
			}
			return required(val);
		},
		requiredForCategory: function(categoryName){
			return function(val, instance, episode){
				/*
				* If something is only required for a condition
				* e.g. MMDiagnosisDetails are only required
				* if the category is MM
				*/
				if(episode.category_name === categoryName){
					return required(val);
				}
				return true;
			}
		},
		lessThanOrEqualTo: function(amount){
			return function(val){
				if(_.isNumber(val) && val > amount){
					return false;
				}
				return true;
			}
		},
		greaterThanOrEqualTo: function(amount){
			return function(val){
				if(_.isNumber(val) && val < amount){
					return false;
				}
				return true;
			}
		},
		maxLength: function(amount){
			return function(val){
				if(val && val.length > amount){
					return false;
				}
				return true;
			}
		},
		noFuture: function(val){
			if(!val){
				return true
			}
			var today = moment();
			if(toMomentFilter(val).isAfter(today, "d")){
				return false;
			}
			return true;
		},
		sameOrAfterInstanceField: function(instanceField){
			/*
			* Takes the name of a field on the instance, returns
			* true if the field on the instance is before the val.
			* e.g.
			* for BoneDisease.end_date you could add the validator rule
			* sameOrAfterInstanceField('start_date')
			*/
			return function(val, instance){
				if(!val || !instance[instanceField]){
					return true
				}
				if(toMomentFilter(instance[instanceField]).isAfter(toMomentFilter(val), "d")){
					return false;
				}
				return true;
			}
		},
		responseToRegimens: function(val, instance, episode){
			/*
			* From the perspective of a response_date, validates that there
			* is a regimen related to it.
			*/
			if(!val){
				return true;
			}
			var withinRegimen = false;
			_.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
				var within = responseDateWithRegimen(val, regimen);
				if(within){
					withinRegimen = true;
				}
			});
			return withinRegimen
		},
		inOptions: function(value, instance, episode, patient, apiName, fieldName, schema, lookuplists){
			/*
			* If a model field has choices or is connected to a lookup list
			* this makes sure that the value in the field is within the
			* choices/lookup list
			*/
			if(!value){
				return true;
			}
			var subRecordSchema = _.findWhere(schema[apiName].fields, {name: fieldName});
			if(subRecordSchema.enum){
				return _.contains(subRecordSchema.enum, value)
			}

			var lookupListName = subRecordSchema.lookup_list;
			if(lookupListName){
				return _.contains(lookuplists[lookupListName], value)
			}

			return true;
		}
	}
});
