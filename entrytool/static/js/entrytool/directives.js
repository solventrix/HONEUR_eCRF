!(function () {
  "use strict";
  directives.directive("dateAfter", function ($parse, toMomentFilter) {
    /*

    This data validation directive is intended for use with the
    custom datepicker field.

    It will invalidate the field if the value of the input this
    directive is attached to is after the date in another field.

    It takes an argument of a second date field to compare with, and
    an optional offset when comparing.

    date-after="startDate" date-after-diff="30"

  */
    return {
      require: "ngModel",
      link: function (scope, elm, attrs, ctrl, ngModel) {
        scope.$watch(
          function () {
            return $parse(attrs.dateAfter)(scope);
          },
          function () {
            ctrl.$validate();
          }
        );

        ctrl.$validators.dateAfter = function (modelValue, viewValue) {
          var before = toMomentFilter($parse(attrs.dateAfter)(scope));
          var dateAfterDiff = 1;
          if (attrs.dateAfterDiff) {
            dateAfterDiff = parseInt(attrs.dateAfterDiff);
          }
          if (before) {
            var b = before.add(dateAfterDiff, "d");
            if (viewValue) {
              viewValue = toMomentFilter(viewValue);
              if (viewValue < b) {
                return false;
              }
            }
          }
          return true;
        };
      },
    };
  });

  directives.directive("dateBefore", function ($parse, toMomentFilter) {
    /*

    This data validation directive is intended for use with the
    custom datepicker field.

    It will invalidate the field if the value of the input this
    directive is attached to is before the date in another field.

    It takes an argument of a second date field to compare with, and
    an optional offset when comparing.

    date-before="startDate" date-before-diff="30"

  */
    return {
      require: "ngModel",
      link: function (scope, elm, attrs, ctrl, ngModel) {
        scope.$watch(
          function () {
            return $parse(attrs.dateBefore)(scope);
          },
          function () {
            ctrl.$validate();
          }
        );

        ctrl.$validators.dateBefore = function (modelValue, viewValue) {
          var before = toMomentFilter($parse(attrs.dateBefore)(scope));
          dateBeforeDiff = 1;
          if (attrs.dateBeforeDiff) {
            dateBeforeDiff = parseInt(attrs.dateBeforeDiff);
          }

          if (before) {
            b = before.add(dateBeforeDiff, "d");
            if (viewValue) {
              viewValue = toMomentFilter(viewValue);
              if (viewValue > b) {
                return false;
              }
            }
          }
          return true;
        };
      },
    };
  });

  var regimenDateBetween = function (fieldValue, instance, episode, patient) {
    /*
     * Takes in a field value (a moment), instance(a regimen) and a patient
     * Returns true if the field is between start/end of two
     * regimen dates and is not the same regimen
     */
    var error = false;
    if (!fieldValue) {
      return error;
    }
    _.each(patient.episodes, function (episode) {
      _.each(episode.regimen, function (r) {
        if (r.id !== instance.id) {
          if (r.start_date && r.end_date) {
            if (fieldValue >= r.start_date && fieldValue <= r.end_date) {
              error = true;
            }
          }
        }
      });
    });

    return error;
  };

  var regimenSurrounds = function (fieldValue, instance, episode, patient) {
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
    var startDate = instance.start_date;
    var endDate = instance.end_date;
    if(!startDate && !endDate){
      return error;
    }
    _.each(patient.episodes, function (episode) {
      _.each(episode.regimen, function (r) {
        if (r.id !== instance.id) {
          if (r.start_date && r.end_date) {
            if (startDate < r.start_date && endDate > r.end_date) {
              error = true;
            }
          }
        }
      });
    });
    return error;
  };

  directives.directive("regimenStart", function ($parse, toMomentFilter) {
    var VALIDATORS = {
      regimenDateBetween: regimenDateBetween,
      regimenSurrounds: regimenSurrounds
    };
    return {
      require: "ngModel",
      link: function (scope, elm, attrs, ctrl, ngModel) {
        _.each(VALIDATORS, function (v, k) {
          ctrl.$validators[k] = function (modelValue, viewValue) {
            var viewDate = toMomentFilter(viewValue);
            return !v(
              viewDate,
              scope.item,
              scope.the_episode,
              scope.$root.patient
            );
          };
        });
      },
    };
  });
})();
