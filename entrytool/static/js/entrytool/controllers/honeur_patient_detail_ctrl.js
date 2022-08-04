angular.module('opal.controllers').controller("HoneurPatientDetailCtrl", function($scope, $rootScope, ValidatePatient){
	"use strict";
	var self = this;

	// if subrecords have been imported and have been
	// marked as errors. We store which subrecords
	// have errored with [(episodeId, subrecordApiName, subrecordId)]
	this._erroringSubrecords = []

	this.editItem = function(item_name, item, episode){
		/*
		* Wraps edit item to clean the patient validator after a subrecord has
		* been saved.
		*/
		return episode.recordEditor.editItem(item_name, item).then(function(){
			$rootScope.patientValidator.clean();
			if(self._erroringSubrecords.length){
				self.checkPatient();
			}
		});
	}

	this.checkPatient = function(){
		/*
		* if a patient load object states the patient has errors from a
		* file import, run the validate patient.
		*
		* if this finds errors, we store the erroring subrecord(s) in an
		* array on this._erroringSubrecords
		*
		* otherwise the ValidatePatient.validatePatient will update the backend
		* to say the patient has no errors.
		*/
		if($scope.patient.patient_load[0].source === 'Loaded From File'){
			if($scope.patient.patient_load[0].has_errors){
				ValidatePatient.validatePatient($scope.patient).then(function(errors){
					self._erroringSubrecords = errors;
				});
			}
		}
	}
	this.hasError = function(episodeId, subrecordApiName, subrecordId){
		var result = false;
		_.each(this._erroringSubrecords, function(err){
			// The below is just cross browser array equality
			if(JSON.stringify(err) == JSON.stringify([episodeId, subrecordApiName, subrecordId])){
				result = true;
			}
		})
		return result;
	}
	this.checkPatient();
});
