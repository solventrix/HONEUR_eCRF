angular.module('opal.controllers').controller("HoneurPatientDetailCtrl", function($scope, $rootScope, $modal, $q, UserProfile, ValidatePatient, EntryToolRecordEditor){
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
		var recordEditor = new EntryToolRecordEditor($rootScope.patientValidator, episode);
		return recordEditor.editItem(item_name, item).then(function(){
			if(self._erroringSubrecords.length){
				self.checkPatient();
			}
		});
	}

	this.newItem = function(item_name, episode){
		var recordEditor = new EntryToolRecordEditor($rootScope.patientValidator, episode);
		return recordEditor.newItem(item_name)
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


	this.showDataQualityReviewed = function(){
		if(self._erroringSubrecords.length){
			var episode = $scope.patient.episodes[0]
			if(!episode.patient_load[0].data_quality_reviewed){
				return true
			}
		}
		return false;
	}



	this.openDataQualityReviewedModal = function(){
		var deferred = $q.defer();
		UserProfile.load().then(function(profile){
			var episode = $scope.patient.episodes[0];
			if(profile.readonly){
					deferred.resolve();
			}
			else{
				var modal_opts = {
						backdrop: 'static',
						templateUrl: "entrytool/templates/modals/data_quality_reviewed.html",
						controller: "DataQualityReviewedCtrl",
						resolve: {
								item: episode.patient_load[0],
						}
				};

				var modal = $modal.open(modal_opts);

				modal.result.then(function(result) {
					$q.when(result).then(function(x){
						$rootScope.state = 'normal';
						deferred.resolve(result);
					});
				});
			}
		});
		return deferred.promise;

	};

	this.checkPatient();
});
