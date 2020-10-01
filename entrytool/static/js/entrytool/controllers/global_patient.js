angular
  .module("opal.controllers")
  .controller("GlobalPatient", function ($scope, $rootScope) {
    "use strict";
    /*
    * hoist the patient so we can easily validate it.
    */
    $rootScope.patient = $scope.patient;
  });
