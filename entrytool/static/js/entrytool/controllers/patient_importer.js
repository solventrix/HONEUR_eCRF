angular
  .module("opal.controllers")
  .controller("PatientImporter", function (
    $scope, $q, patientLoader, ValidatePatient, unValidatedPatients, patientsWithErrors
  ) {
    "use strict";

    // a list of unvalidate patient ids
    $scope.unvalidatedPatients = unValidatedPatients;

    // a list of patient ids with errors
    $scope.patientsWithErrors = patientsWithErrors;

    // the initial number of unvalidated patients
    $scope.initialUnvalidatedCount = 0;

    // the number of patients we have currently validated
    $scope.validaterPointer = 0;

    var init = function(){
      /*
      * Load in all unvalidated patients and patients with errors.
      * Iterate over the unvalidated patients and start validating them.
      */
      $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
      process()
    }

    var processPatientId = function(unvalidatedPatientId){
      /*
      * Take an unvalidated patient, load the patient, validate them and
      * update the pointer and the patientWithErrors if necessary.
      */
      var deferred = $q.defer()
      patientLoader(unvalidatedPatientId).then(ValidatePatient.validatePatient).then(function(errors){
        if(errors.length){
          $scope.patientsWithErrors.push(unvalidatedPatientId)
        }
        $scope.validaterPointer += 1;
        deferred.resolve()
      });
      return deferred.promise;
    }

    var process = function(){
      /*
      * Iterate through all unvalidated patients and process them one after
      * another.
      */
      var deferred = $q.defer()
      deferred.resolve();
      var promise = deferred.promise;
      _.each($scope.unvalidatedPatients, function(unvalidatedPatientId){
        // chain the promises so that we resolve them one after another
        promise = promise.then(function(){ return processPatientId(unvalidatedPatientId)});
      });
    }

    init();
  });
