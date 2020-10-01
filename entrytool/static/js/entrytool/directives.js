directives.directive('dateAfter', function($parse, toMomentFilter) {
  /*
  * checks the model attatched to the field is after the field passed in
  * e.g. if the model is endDate, date-after="startDate"
  *
  * if the model should be 30 days after the start date
  * date-after="startDate" date-after-diff="30"
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
          return true;
        }
      }
    }
  };
});


directives.directive('dateBefore', function($parse, toMomentFilter) {
  /*
  * checks the model attatched to the field is before the field passed in
  * e.g. if the model is startDate, date-before="endDate"
  *
  * if the model should be 30 days before the end date
  * date-before="endDate" date-before-diff="30"
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
          return true;
        }
      }
    }
  };
});

