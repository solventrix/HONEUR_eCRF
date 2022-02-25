angular
  .module("opal.controllers")
  .controller("PatientValidator", function (
    $scope,
    $rootScope,
    toMomentFilter,
    EntrytoolHelper,
    $injector
  ) {
    "use strict";

    var VALDATION_ERRORS = $injector.get('VALDATOR_ERRORS');

    var PatientValidator = function () {
      var self = this;
      self.entrytool_helper = EntrytoolHelper;

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
              if(!someFunc){
                return;
              }
              // if there was a previous error, let's use the first
              // we hit.
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
            result = null;
          })
        }
        self[fieldName] = checkError;
      };

      var validateRegimenDateBetween = function (
        fieldValue,
        instance
      ) {
        /*
         * Takes in a field value (a moment), instance(a regimen)
         * Returns true if the field is between start/end of two
         * regimen dates and is not the same regimen
         */
        var error = false;
        if (!fieldValue) {
          return error;
        }
        _.each(self.patient.episodes, function (episode) {
          _.each(EntrytoolHelper.getEpisodeRegimen(episode), function (r) {
            if (r.id !== instance.id) {
              if (r.start_date && r.end_date) {
                if (fieldValue >= r.start_date && fieldValue <= r.end_date) {
                  error = true;
                }
              }
            }
          });
        });

        if (error) {
          return VALDATION_ERRORS.REGIMEN_OVERLAP;
        }
      };

      var validateRegimenSurrounds = function (
        fieldValue,
        instance
      ) {
        /*
         * Make sure that when a regimen date is changed, the regimen does not
         * now encompass another regimen
         *
         * Step 1. Create a regimen A but don't but an end date on it with
         * start time Monday.
         * Step 2. Create a regimen B that lasts between Tuesday-Wednesday
         * Step 3. The add an end date on A of Thursday. It should error.
         */
        var error = false;
        if (!fieldValue) {
          return;
        }
        _.each(self.patient.episodes, function (episode) {
          _.each(EntrytoolHelper.getEpisodeRegimen(episode), function (r) {
            if (r.id !== instance.id) {
              if (r.start_date && r.end_date) {
                if (
                  instance.start_date < r.start_date &&
                  instance.end_date > r.end_date
                ) {
                  error = true;
                }
              }
            }
          });
        });
        if (error) {
          return VALDATION_ERRORS.REGIMEN_OVERLAP;
        }
      };

      var responseDateWithRegimen = function(fieldValue, regimen){
        /*
        * A response date can be start_date - 30 days or
        * end_date + 30 days and anything in between.
        */
        var allowedStartDate = moment(regimen.start_date,).add(-30, "d")
        var allowedEndDate = null;
        var withinParams = false;
        if(regimen.end_date){
          allowedEndDate = moment(regimen.end_date).add(30, "d")
          if(fieldValue >= allowedStartDate && fieldValue <= allowedEndDate){
            withinParams = true;
          }
        }
        else{
          if(fieldValue >= allowedStartDate){
            withinParams = true
          }
        }
        return withinParams
      }

      var validateResponseToRegimens = function(val, instance, episode){
        /*
        * From the perspective of a response_date, validates that there
        * is a regimen related to it.
        */
        var withinRegimen = false;
        _.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
          var within = responseDateWithRegimen(val, regimen);
          if(within){
            withinRegimen = true;
          }
        });
        if(!withinRegimen){
          return VALDATION_ERRORS.NO_REGIMEN_RESPONSE;
        }
      }

      var validateRegimenToResponses = function(val, instance, episode){
        /*
        * From the perspective of a regimen, validates that the
        * responses are connected to either other regimens
        * or the regimen in the form.
        */
       if(!val || !EntrytoolHelper.getEpisodeResponse(episode).length){
          return;
       }
        var withinRegimen = false;
        // we may be editing things so ignore version of regimen
        // we are using that is attatched to the episode.
        var regimens = _.reject(EntrytoolHelper.getEpisodeRegimen(episode), {id: instance.id, episode_id: instance.episode_id});
        regimens.push(instance);
        _.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
          if(response.response_date){
            _.each(regimens, function(regimen){
              var within = responseDateWithRegimen(response.response_date, regimen);
              if(within){
                withinRegimen = true;
              }
            });
          }
        });
        if(!withinRegimen){
          return VALDATION_ERRORS.NO_RESONSE_REGIMEN;
        }
      }

      var validateDateOfDiagnosis = function(val, instance, episode){
        /*
        * Date of diagnosis must be below all SCT/Regimen/response dates.
        */
        var error_msg = null;
        _.each(self.patient.episodes, function(episode){
          _.each(EntrytoolHelper.getEpisodeRegimen(episode), function(regimen){
            if(regimen.start_date < val){
              error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_REGIMEN_START
            }
          });
        })
        if(error_msg){
          return error_msg
        }
        var error_msg = null;
        _.each(self.patient.episodes, function(episode){
          _.each(episode.sct, function(sct){
            if(sct.sct_date < val){
              error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_SCT;
            }
          });
        })
        if(error_msg){
          return error_msg
        }

        var error_msg = null;
        _.each(self.patient.episodes, function(episode){
          _.each(EntrytoolHelper.getEpisodeResponse(episode), function(response){
            if(response.response_date < val){
              error_msg = VALDATION_ERRORS.DIAGNOSIS_OVER_RESPONSE;
            }
          });
        })
        if(error_msg){
          return error_msg
        }
      };

      self.validateOnlyOneOpenRegimen = function(val, instance, episode){
        /*
        * There can only be one regimen with no end date, if the user
        * is trying to save a regimen with no end date and there
        * already exists another with no end date, flag it as an error.
        *
        * Note this is a special case of validation as it exists as part of an
        * ng-required not ng-change like the rest of the validation.
        *
        * It returns null if there is no error, or true if there is an error
        */

        // if there is a val then there is an end date for this
        // regimen and we don't need to check the other episodes
        if(val){
          return
        }
        var regimen = EntrytoolHelper.getEpisodeRegimen(episode);

        // exclude the current regimen if it has already been saved
        if(instance.id){
          regimen = _.without(regimen, {id: instance.id});
        }

        var noEndDate = _.filter(regimen, function(r){
          if(!r.end_Date){
            return true
          }
        });

        if(noEndDate.length){
          return true
        }
      }

      var episodeRegimenMinMaxDates = function (episode) {
        // returns the first start date and the last end date
        // note end date may be null;

        // pluck the regimen start dates, sort them and return the first
        var episodeMin = _.pluck(EntrytoolHelper.getEpisodeRegimen(episode), "start_date").sort()[0];

        var episodeMax = null;
        // regimen end date is not required, remove the nulls and
        // make sure any of them are populated
        var episodeMaxVals = _.compact(_.pluck(EntrytoolHelper.getEpisodeRegimen(episode), "end_date"));
        if (episodeMaxVals.length) {
          episodeMax = _.sortBy(episodeMaxVals).reverse()[0];
        }
        return [episodeMin, episodeMax];
      };

      var validateRegimenToOtherLOTRegimens = function (
        val,
        instance,
        episode
      ) {
        /*
         * for an episode's regimens they should not overlap another episodes
         * regimens
         */
        // check vs the instance dates as these may have changed.
        var min = toMomentFilter(instance.start_date);
        var max = toMomentFilter(instance.end_date);

        if(EntrytoolHelper.getEpisodeRegimen(episode).length){
          var ourEpisodeMinMax = episodeRegimenMinMaxDates(episode);
          if(ourEpisodeMinMax[0].isBefore(min, "d")){
            min = ourEpisodeMinMax[0];
          }
          if(!max){
            max = ourEpisodeMinMax[1];
          }
          else if (ourEpisodeMinMax[1] && ourEpisodeMinMax[1].isAfter(max, "d")){
            max = ourEpisodeMinMax[1];
          }
        }

        var error = null;

        _.each(self.patient.episodes, function (otherEpisode) {
          if (error) {
            return;
          }
          // ignore this episode
          if (episode.id === otherEpisode.id) {
            return;
          }
          if (!EntrytoolHelper.getEpisodeRegimen(otherEpisode).length) {
            return;
          }
          var episodeMinMax = episodeRegimenMinMaxDates(otherEpisode);
          var episodeMin = episodeMinMax[0];
          var episodeMax = episodeMinMax[1];
          // other episode ends before our episode starts
          if(episodeMax && episodeMax.isBefore(min, "d")){
            return;
          }
          // other episode does not have a start but starts before our episode starts
          if(!episodeMax && episodeMin.isBefore(min, "d")){
            return;
          }
          // our episode ends before other episode starts
          if(max && max.isBefore(episodeMin, "d")){
            return;
          }
          // our episode has no end but starts before other episode starts
          if(!max && min.isBefore(episodeMin, "d")){
            return;
          }
          error = VALDATION_ERRORS.REGIMEN_OVERLAPS;
        });
        return error;
      };

      this.clean = function(){
        self.errors = {};
        self.warnings = {};
      }

      this.setUp = function () {
        this.patient = $scope.patient;
        this.clean()

        this.hasError = function () {
          return _.size(self.errors);
        };
        this.createValidator(
          "regimen_start", {
            errors: [validateRegimenDateBetween, validateRegimenSurrounds, validateRegimenToOtherLOTRegimens],
            warnings: [validateRegimenToResponses]
          }
        )
        this.createValidator(
          "regimen_end", {
            errors: [validateRegimenDateBetween, validateRegimenSurrounds, validateRegimenToOtherLOTRegimens],
            warnings: [validateRegimenToResponses]
          }
        );
        this.createValidator(
          "response_date", {
            warnings: [validateResponseToRegimens]
          }
        );
        this.createValidator(
          "diagnosis_date", {
            errors: [validateDateOfDiagnosis]
          }
        );
      };
      this.setUp();
    };
    $rootScope.patientValidator = new PatientValidator();
  });
