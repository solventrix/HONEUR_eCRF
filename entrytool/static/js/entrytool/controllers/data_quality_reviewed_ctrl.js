angular
  .module("opal.controllers")
  .controller(
    "DataQualityReviewedCtrl",
    function ($scope, $modalInstance, item) {
      "use strict";
			$scope.item = item;
      $scope.save = function () {
        var patientLoad = item.makeCopy();
        patientLoad.data_quality_reviewed = true;
        patientLoad.data_quality_reviewed_date = new Date();

        item.save(patientLoad).then(function () {
          $modalInstance.close(item);
        });
      };

      $scope.cancel = function () {
        $modalInstance.close("cancel");
      };
    }
  );
