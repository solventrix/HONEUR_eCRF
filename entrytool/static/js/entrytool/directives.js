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
          var dateBeforeDiff = 1;
          if (attrs.dateBeforeDiff) {
            dateBeforeDiff = parseInt(attrs.dateBeforeDiff);
          }

          if (before) {
            var b = before.add(dateBeforeDiff, "d");
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
