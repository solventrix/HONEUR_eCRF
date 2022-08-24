angular
  .module("opal.controllers")
  .controller("DataUploader", function (
    $scope, $q, patientLoader, $http, ValidatePatient, unValidatedPatients, patientsWithErrors, DataUploadLoader
  ) {
    "use strict";

    // a list of unvalidate patient ids
    $scope.unvalidatedPatients = unValidatedPatients;

    // a list of issues with the upload, e.g. a date not formatting correctly
    $scope.uploadErrors = {
      top_level_errors: [],
      row_errors: [],
    };

    // a list of patient ids with errors
    $scope.patientsWithErrors = patientsWithErrors;

    // the initial number of unvalidated patients
    $scope.initialUnvalidatedCount = 0;

    // if we are in the state of validating patients rather than
    // offering the upload form
    $scope.validatingPatients = false

    // the number of patients we have currently validated
    $scope.validaterPointer = 0;
    $scope.loading = false;

    //
    // The template has four panels to display the UI for uploading
    // data - only one should be visible at any time
    //
    $scope.uploadSections = {
      LOADING: "LOADING",
      VALIDATING: "VALIDATING",
      UPLOAD_ISSUES: "UPLOAD_ISSUES",
      UPLOAD_FORM: "UPLOAD_FORM"
    }

    //
    // This function avoids the need to check multiple flags
    // in the template ng-show expressions
    //
    $scope.showSection = function(name){
      if($scope.loading){
          return $scope.uploadSections.LOADING == name;
      }
      if($scope.errorCount()){
          return $scope.uploadSections.UPLOAD_ISSUES == name;
      }
      if($scope.initialUnvalidatedCount){
        return $scope.uploadSections.VALIDATING == name;
      }
      return $scope.uploadSections.UPLOAD_FORM == name;
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
      patientLoader(unvalidatedPatientId).then(ValidatePatient.validatePatient).then(function(){
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

      promise = promise.then(function(){
        DataUploadLoader.patientsWithErrors().then(function(patientsWithErrors){
          $scope.patientsWithErrors = patientsWithErrors;
        });
      });
    }

    $scope.setLoading = function(){
      $scope.loading = true;
    }

    $scope.errorCount = function(){
      return $scope.uploadErrors.top_level_errors.length + $scope.uploadErrors.row_errors.length
    }

    $scope.reset = function(){
      $scope.uploadErrors = {
        top_level_errors: [],
        row_errors: [],
      };
    }

    $scope.formSubmitCallback = function(response){
      if(response.data.top_level_errors.length || response.data.row_errors.length){
        $scope.loading = false;
        $scope.uploadErrors = response.data
      }
      else{
        $scope.validatingPatients = true;
        DataUploadLoader.unValidatedPatients().then(function(responseData){
          $scope.loading = false;
          $scope.unvalidatedPatients = responseData;
          $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
          process();
        });
      }
    }

    init();
  });
