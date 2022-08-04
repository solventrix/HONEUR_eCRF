angular.module('opal.services').factory('ValidatePatient', function(
	$q, recordLoader, ValidateField
) {
	"use strict";
	/*
	* Checks if a patient has any errors using the ValidateField service.
	*
	* Updates the PatientLoad singleton for the patient if they were
	* previous not validated or they previously had errors that have
	* now been resolved.
	*/

	var _validatePatient = function(schema, patient){
		var errors = []
		_.each(patient, function(model, modelApiName){
			if(!_.isArray(model)){
				return
			}
			if(modelApiName === 'episodes'){
				_.each(model, function(episode){
					_.each(episode, function(subrecords, subrecordApiName){
						if(!_.isArray(subrecords)){
							return
						}
						if(subrecordApiName === 'tagging'){
							return;
						}
						_.each(subrecords, function(episodeSubrecord){
							_.each(schema[subrecordApiName].fields, function(field){
								var errorMessages = ValidateField.validate(
									subrecordApiName,
									field["name"],
									episodeSubrecord[field["name"]],
									episodeSubrecord,
									episode,
									patient
								);

								if(errorMessages.length){
									errors.push([episode.id, subrecordApiName, episodeSubrecord.id])
								}
							});
						})
					})
				});
			}
		});
		return errors;
	}

	var updatePatientLoadIfRequired = function(patient, errors){
		var result = $q.defer();
		var episode = _.values(patient.episodes)[0]
		var patientLoad = episode.patient_load[0];
		var needsAnUpdate = false;
		if(!patientLoad.validated ){
			needsAnUpdate = true
		}
		if(patientLoad.has_errors && !errors.length){
			needsAnUpdate = true
		}
		if(needsAnUpdate){
			var copy = patientLoad.makeCopy();
			copy.has_errors = !!errors.length;
			copy.validated = true;
			patientLoad.save(copy).then(function(){
				result.resolve();
			});
		}
		else{
			result.resolve();
		}
		return result.promise;
	}

	return {
		validatePatient: function(patient){
			var deferred = $q.defer();
			recordLoader.load().then(function(schema){
				var errors = _validatePatient(schema, patient, deferred);
				updatePatientLoadIfRequired(patient, errors).then(function(){
					deferred.resolve(errors);
				})
			})
			return deferred.promise;
		}
	}
});
