directives.directive('dateAfter', function($parse, toMomentFilter) {
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
    require: 'ngModel',
    link: function(scope, elm, attrs, ctrl, ngModel) {
      scope.$watch(function () {
        return $parse(attrs.dateAfter)(scope);
      }, function () {
          ctrl.$validate();
      });

      ctrl.$validators.dateAfter = function(modelValue, viewValue){
        var before = toMomentFilter($parse(attrs.dateAfter)(scope));
        dateAfterDiff = 1;
        if(attrs.dateAfterDiff){
          dateAfterDiff = parseInt(attrs.dateAfterDiff);
        }
        if(before){
          b = before.add(dateAfterDiff, "d");
          if(viewValue){
            viewValue = toMomentFilter(viewValue);
            if(viewValue < b){
              return false;
            }
          }
        }
        return true;
      }
    }
  };
});


directives.directive('dateBefore', function($parse, toMomentFilter) {
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
    require: 'ngModel',
    link: function(scope, elm, attrs, ctrl, ngModel) {
      scope.$watch(function () {
        return $parse(attrs.dateBefore)(scope);
      }, function () {
          ctrl.$validate();
      });

      ctrl.$validators.dateBefore = function(modelValue, viewValue){
        var before = toMomentFilter($parse(attrs.dateBefore)(scope));
        dateBeforeDiff = 1;
        if(attrs.dateBeforeDiff){
          dateBeforeDiff = parseInt(attrs.dateBeforeDiff);
        }

        if(before){
          b = before.add(dateBeforeDiff, "d");
          if(viewValue){
            viewValue = toMomentFilter(viewValue);
            if(viewValue > b){
              return false;
            }
          }
        }
        return true;
      }
    }
  };
});

directives.directive('regimenBetween', function(toMomentFilter) {
  /*
  * Make sure the model date is not between the other regimen start dates
  */
  return {
    require: 'ngModel',
    link: function(scope, elm, attrs, ctrl) {
      ctrl.$validators.regimenBetween = function(modelValue, viewValue){
        error = true;
        viewValue = toMomentFilter(viewValue);
        if(!viewValue){
          return true;
        }
        _.each(scope.$root.patient.episodes, function(episode){
          _.each(episode.regimen, function(r){
            if(scope.editing.regimen.id === r.id){
              // ignore it if its the one we are talking about.
              return;
            }
            if(r.start_date && r.end_date){
              if(viewValue > r.start_date && viewValue < r.end_date){
                error = false
              }
            }
          });
        });
        return error;
      }
    }
  };
});


directives.directive('regimenEnd', function(toMomentFilter) {
  /*
  * Make sure that the regimen end, once added is not then around
  * another regimen. Its a niche case...
  *
  * Step 1. Create a regimen A but don't but an end date on it with
  * start time Monday.
  * Step 2. Create a regimen B that lasts between Tuesday-Wednesday
  * Step 3. The add an end date on A of Thursday. It should error.
  */
  return {
    require: 'ngModel',
    link: function(scope, elm, attrs, ctrl) {
      ctrl.$validators.regimenEnd = function(modelValue, viewValue){
        viewValue = toMomentFilter(viewValue);
        error = true;
        if(!viewValue){
          return false;
        }
        startDate = toMomentFilter(scope.editing.regimen.start_date);
        if(!startDate){
          return false
        }
        _.each(scope.$root.patient.episodes, function(episode){
          _.each(episode.regimen, function(r){
            if(scope.editing.regimen.id === r.id){
              // ignore it if its the one we are talking about.
              return;
            }
            if(r.start_date && r.end_date){
              if(startDate < r.start_date && viewValue > r.end_date){
                error = false;
              }
            }
          });
        });

        return error;
      }
    }
  };
});


