angular
  .module("opal.controllers")
  .controller("PatientValidator", function (
    $scope,
    $rootScope,
    $q,
    recordLoader,
    Referencedata,
    ValidateField,
  ) {
    "use strict";

    var PatientValidator = function (patient) {
      var self = this;
      self.saveDisabled = false;
      self.submitted = false;
      self.errors = {};
      self.warnings = {};
      self.patient = patient;

      this.validatesubrecord = function(subrecordApiName, subrecord, episode){
        /*
        * Validates a whole subrecord and sets the errors/warnings on itself.errors/warnings
        */
        var result = $q.defer();
        $q.all([recordLoader.load(), Referencedata.load()]).then(function(loadResults){
          var schema = loadResults[0];
          var lookuplists = loadResults[1];

          _.each(schema[subrecordApiName].fields, function(field){
            var issues = ValidateField.validate(
              subrecordApiName,
              field["name"],
              subrecord[field["name"]],
              subrecord,
              episode,
              self.patient,
              schema,
              lookuplists
            )
            self.errors[field["name"]] = issues.errors
            self.warnings[field["name"]] = issues.warnings
          });
          result.resolve();
        });

        return result.promise;
      }

      this.preSaveValidate = function(subrecordApiName, subrecord, episode, someFn){
        self.validatesubrecord(subrecordApiName, subrecord, episode).then(function(){
          if(!_.size(_.filter(self.errors, function(err){ return err.length }))){
            someFn();
          }
          else if(self.patient.patient_load[0].has_errors){
            someFn();
          }
          else{
            self.submitted = true;
          }
        });
      }

      this.clean = function(){
        self.errors = {};
        self.warnings = {};
        self.saveDisabled = false;
        self.submitted = false;
      }

      this.showErrors = function(field_name){
        if(!self.errors[field_name] || !self.errors[field_name].length){
          return false;
        }
        if(self.submitted || self.patient.patient_load[0].has_errors){
          return true;
        }
        return false;
      }

      this.showWarnings = function(field_name){
        if(!self.warnings[field_name]){
          return false;
        }
        return true;
      }

      this.enableSave = function(){
        if(self.patient.patient_load[0].has_errors){
          self.saveDisabled = false;
        }
        if(!self.submitted){
          self.saveDisabled = false;
        }
        if(_.size(_.filter(self.errors, function(err){ return err.length }))){
          self.saveDisabled = true
        }
        else{
          self.saveDisabled = false;
        }
      }
    };
    $rootScope.patientValidator = new PatientValidator($scope.patient);
  });
