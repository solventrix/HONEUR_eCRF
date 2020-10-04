angular
  .module("opal.controllers")
  .controller("PatientValidator", function (
    $scope,
    $rootScope,
  ) {
    "use strict";

    var PatientValidator = function () {
      var self = this;

      this.createValidator = function (fieldName, errorTypeToFunctionList) {
        /*
        * takes in a fieldName and an object of {errorType: [validationFuns]}
        *
        * wraps them so that any results from validation funs are put on
        * self[errorType][fieldName]
        *
        * e.g.
        * createValidator(myField, {errors: [someFunThatReturnsBoom]}
        *
        * when called with an ng change will set self.errors.myField == "Boom"
        *
        * If the function returns nothing then the key is deleted from self
        */
        var checkError = function (fieldValue, instance, episode) {
          var result = null;
          var errorTypes = ["errors", "warnings"]
          _.each(errorTypes, function(errorType){
            _.each(errorTypeToFunctionList[errorType], function (someFunc) {
              if(result){
                return;
              }
              result = someFunc(fieldValue, instance, episode, fieldName);
            });
            if(result){
              self[errorType][fieldName] = result;
            }
            else{
              delete self[errorType][fieldName];
            }
          })
        }
        self[fieldName] = checkError;
      };

      this.clean = function(){
        this.errors = {};
        this.warnings = {};
      }

      this.setUp = function () {
        this.patient = $scope.patient;
        this.clean()

        this.hasError = function () {
          return _.size(self.errors);
        };
      };
      this.setUp();
    };
    $rootScope.patientValidator = new PatientValidator();
  });
