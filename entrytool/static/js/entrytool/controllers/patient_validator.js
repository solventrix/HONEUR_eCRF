angular
  .module("opal.controllers")
  .controller("PatientValidator", function (
    $scope,
    $rootScope,
    $q,
    ValidateField,
    recordLoader
  ) {
    "use strict";

    var PatientValidator = function (patient) {
      var self = this;
      self.saveDisabled = false;
      self.submitted = false;
      self.errors = {};
      self.warnings = {};
      self.patient = patient;

      this.validateField = function(apiName, fieldName, value, instance, episode, patient){
        /*
        * validates for different alertTypes which are either warnings or errors
        */
        var result = {
          warnings: [],
          errors: []
        }
        var self = this;
        if(self[apiName] && self[apiName][fieldName]){
          _.each(['warnings', 'errors'], function(alertType){
            if(!ValidationRules[apiName][fieldName][alertType]){
              return;
            }
            _.each(ValidationRules[apiName][fieldName][alertType], function(validator_and_error){
              var validator = validator_and_error[0];
              var error = validator_and_error[1];
              var issue = validator(value, instance, episode, patient);
              if(issue){
                result[alertType].push(error);
              }
            });
          })
        }
        return result;
      }

      this.validatesubrecord = function(subrecordApiName, subrecord, episode){
        /*
        * Validates a whole subrecord and sets the errors/warnings on itself.errors/warnings
        */
        var result = $q.defer();
        recordLoader.load().then(function(schema){
          _.each(schema[subrecordApiName].fields, function(field){
            var issues = ValidateField.validate(
              subrecordApiName,
              field["name"],
              subrecord[field["name"]],
              subrecord,
              episode,
              self.patient
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

      this.validate = function(model_api_name, field_name, val, instance, episode){
        var issues = ValidateField.validate(
          model_api_name,
          field_name,
          val,
          instance,
          episode,
          self.patient
        )
        self.errors[field_name] = issues.errors;
        self.warnings[field_name] = issues.warnings;
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
