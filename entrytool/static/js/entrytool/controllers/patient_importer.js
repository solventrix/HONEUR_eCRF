angular
  .module("opal.controllers")
  .controller("PatientImporter", function (
    $scope, $http, $q, patientLoader, ValidatePatient
  ) {
    "use strict";

    // a list of unvalidate patient ids
    $scope.unvalidatedPatients = [];

    // a list of patient ids with errors
    $scope.patientsWithErrors = [];

    // the initial number of unvalidated patients
    $scope.initialUnvalidatedCount = 0;

    // the number of patients we have currently validated
    $scope.validaterPointer = 0;

    var init = function(){
      /*
      * Load in all unvalidated patients and patients with errors.
      * Iterate over the unvalidated patients and start validating them.
      */
      var unValidatedPatientsPromise = $http.get('/entrytool/v0.1/unvalidated_patients/');
      var patientsWithErrorsPromise = $http.get('/entrytool/v0.1/patients_with_errors/');
      $q.all([unValidatedPatientsPromise, patientsWithErrorsPromise]).then(function(result){
        $scope.unvalidatedPatients = result[0].data;
        $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
        $scope.patientsWithErrors = result[1].data;
        process()
      })
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
