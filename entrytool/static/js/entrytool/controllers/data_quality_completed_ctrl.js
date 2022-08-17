angular
  .module("opal.controllers")
  .controller(
    "DataQualityCompletedCtrl",
    function ($scope, $modalInstance, item) {
      "use strict";
			$scope.item = item;
      $scope.save = function () {
        var patientLoad = item.makeCopy();
        patientLoad.data_quality_completed = true;
        patientLoad.data_quality_completed_date = new Date();

        item.save(patientLoad).then(function () {
          $modalInstance.close(item);
        });
      };

      $scope.cancel = function () {
        $modalInstance.close("cancel");
      };
    }
  );
