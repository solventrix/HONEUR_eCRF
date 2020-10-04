angular
  .module("opal.controllers")
  .controller("PatientValidator", function (
    $scope,
    $rootScope,
  ) {
    "use strict";
    var PatientValidator = function () {
      var self = this;


      this.setUp = function () {
        this.patient = $scope.patient;
        this.errors = {};
        this.warnings = {};
        this.hasError = function () {
          return _.size(self.errors);
        };

      };
      this.setUp();
    };
    $rootScope.patientValidator = new PatientValidator();
  });
