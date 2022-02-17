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

  directives.directive("noFuture", function (toMomentFilter) {
    /*
     * A directive that will error if the field is in the future
     */
    return {
      require: "ngModel",
      link: function (scope, elm, attrs, ctrl, ngModel) {
        ctrl.$validators.noFuture = function (modelValue, viewValue) {
          var viewValue = toMomentFilter(viewValue);
          if(!viewValue){
            return true
          }
          var now = moment();
          if (viewValue.isAfter(now, "d")) {
            return false;
          }
          return true;
        };
      },
    };
  });

  directives.directive("beforeDeath", function(toMomentFilter){
    /*
    * A directive that will error if the field is > date of death
    */
    return {
      require: "ngModel",
      link: function (scope, elm, attrs, ctrl, ngModel) {

        if(scope.editing.patient_status){
          // if we are editing the patient details recalculate
          // the validation if the death_date changes.
          scope.$watch("editing.patient_status.death_date", function(){
            ctrl.$validate();
          });
        }

        ctrl.$validators.beforeDeath = function (modelValue, viewValue) {
          var viewValue = toMomentFilter(viewValue);
          if(!viewValue){
            return true;
          }
          var deathDate;
          // if we're editing patient details then look
          // at what is in the form at present.
          if(scope.editing.patient_status){
            deathDate = scope.editing.patient_status.death_date;
          }
          else{
            deathDate = scope.the_episode.patient_status[0].death_date;
          }
          if(!deathDate){
            return true
          }
          var viewValue = toMomentFilter(viewValue);
          if (viewValue.isAfter(deathDate, "d")) {
            return false;
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
          var dateBeforeDiff = 1;
          if (attrs.dateBeforeDiff) {
            dateBeforeDiff = parseInt(attrs.dateBeforeDiff);
          }

          if (before) {
            var b = before.subtract(dateBeforeDiff, "d");
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
})();
