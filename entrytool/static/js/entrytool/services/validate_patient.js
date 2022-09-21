angular.module('opal.services').factory('ValidatePatient', function(
	$q, recordLoader, Referencedata, ValidateField
) {
	"use strict";
	/*
	* Checks if a patient has any errors using the ValidateField service.
	*
	* Updates the PatientLoad singleton for the patient if they were
	* previous not validated or they previously had errors that have
	* now been resolved.
	*/

	var _validatePatient = function(schema, lookuplists, patient){
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
								// only validate patient subrecords once and do it against the
								// condition episode category. IE ignore patient
								// subrecords on line of treatments
								if(patient[subrecordApiName] && episode.category_name == "Treatment Line"){
									return;
								}
								var errorMessages = ValidateField.validate(
									subrecordApiName,
									field["name"],
									episodeSubrecord[field["name"]],
									episodeSubrecord,
									episode,
									patient,
									schema,
									lookuplists
								).errors;

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
		// Always use the condition episode for patient subrecords
		var episode = _.findWhere(_.values(patient.episodes), function(episode){
			episode.category_name !== "Treatment Line"
		});
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
				patient.patient_load[0] = patientLoad;
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
			$q.all([recordLoader.load(), Referencedata.load()]).then(function(loadResults){
				var schema = loadResults[0];
				var lookuplists = loadResults[1];
				var errors = _validatePatient(schema,lookuplists, patient);
				updatePatientLoadIfRequired(patient, errors).then(function(){
					deferred.resolve(errors);
				})
			})
			return deferred.promise;
		}
	}
});
