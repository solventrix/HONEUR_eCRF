angular
  .module("opal.controllers")
  .controller("DeleteLOTConfirmationCtrl", function (
    $scope,
    $modalInstance,
    $http,
    episode
  ) {
    $scope.destroy = function () {
      var url =
        "/entrytool/v0.1/delete_line_of_treatment_episode/" + episode.id + "/";
      $http.delete(url).then(
        function () {
          $modalInstance.close("deleted");
        },
        function () {
          alert("Unable to create a line of treatment");
          $modalInstance.close("cancel");
        }
      );
    };

    $scope.cancel = function () {
      $modalInstance.close("cancel");
    };
  });
