angular
  .module("opal.controllers")
  .controller("DataUploader", function (
    $scope, $q, patientLoader, $http, ValidatePatient, unValidatedPatients, patientsWithErrors, DataUploadLoader
  ) {
    "use strict";

    // a list of unvalidate patient ids
    $scope.unvalidatedPatients = unValidatedPatients;

    // a list of issues with the upload, e.g. a date not formatting correctly
    $scope.uploadErrors = [];

    // a list of patient ids with errors
    $scope.patientsWithErrors = patientsWithErrors;

    // the initial number of unvalidated patients
    $scope.initialUnvalidatedCount = 0;

    // if we are in the state of validating patients rather than
    // offering the upload form
    $scope.validatingPatients = false

    // the number of patients we have currently validated
    $scope.validaterPointer = 0;
    var loading = false;

    $scope.states = {
      LOADING: "LOADING",
      VALIDATING: "VALIDATING",
      UPLOAD_ISSUES: "UPLOAD_ISSUES",
      UPLOAD_FORM: "UPLOAD_FORM"
    }

    $scope.getState = function(){
      if(loading){
        return $scope.states.LOADING
      }
      if($scope.uploadErrors.length){
        return $scope.states.UPLOAD_ISSUES
      }
      if($scope.initialUnvalidatedCount){
        return $scope.states.VALIDATING;
      }
      return $scope.states.UPLOAD_FORM;
    }

    var init = function(){
      /*
      * Load in all unvalidated patients and patients with errors.
      * Iterate over the unvalidated patients and start validating them.
      */
      $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
      $scope.validatingPatients = !!$scope.initialUnvalidatedCount;
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

    $scope.submit = function(folder){
      if(!folder || !folder.length){
        return;
      }
      else{
        loading = true;
        $http.post('/entrytool/v0.1/upload_from_file_path/', {"folder": folder}).then(function(response){
          if(response.data.length){
            loading = false;
            $scope.uploadErrors = response.data
          }
          else{
            $scope.validatingPatients = true;
            DataUploadLoader.unValidatedPatients().then(function(responseData){
              loading = false;
              $scope.unvalidatedPatients = responseData;
              $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
              process();
            });
          }
        });
      }
    }

    init();
  });
