angular
  .module("opal.controllers")
  .controller("PatientImporter", function (
    $scope, $http, $q, patientLoader, ValidatePatient
  ) {

    $scope.unvalidatedPatients = [];
    $scope.patientsWithErrors = [];
    $scope.initialUnvalidatedCount = null;
    $scope.validaterPointer = 0;

    var init = function(){
      var unValidatedPatientsPromise = $http.get('/entrytool/v0.1/unvalidated_patients/');
      var patientsWithErrorsPromise = $http.get('/entrytool/v0.1/patients_with_errors/');
      $q.all([unValidatedPatientsPromise, patientsWithErrorsPromise]).then(function(result){
        $scope.unvalidatedPatients = result[0].data;
        $scope.initialUnvalidatedCount = $scope.unvalidatedPatients.length;
        $scope.patientsWithErrors = result[1].data;
        process()
      })
    }

    var process = function(){
      _.each($scope.unvalidatedPatients, function(unvalidatedPatientId){
        patientLoader(unvalidatedPatientId).then(ValidatePatient.validatePatient).then(function(errors){
          if(errors.length){
            $scope.patientsWithErrors.push(unvalidatedPatientId)
          }
          $scope.validaterPointer += 1;
        });
      });
    }

    init();
  });
