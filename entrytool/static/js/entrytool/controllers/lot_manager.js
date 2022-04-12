angular.module('opal.controllers').controller(
  "LineOfTreatmentManager", function($scope, $http, $q, $modal, toMomentFilter, UserProfile, EntrytoolHelper){
    "use strict";
    var self = this;
    this.loading = false;
    this.readonly = false;
    UserProfile.load().then(function(profile){
      self.readonly = profile.readonly;
    });

    this.canEdit = function(){
      return !this.loading && !this.readonly;
    }

    this.create = function(patient){
      this.loading = true;
      var deferred = $q.defer();
      var url = "/entrytool/v0.1/new_line_of_treatment_episode/" + patient.id + "/";
      $http.put(url).then(function(){
        $scope.refresh().then(function(){
          self.loading = false;
          deferred.resolve();
        });
      }, function(){
        self.loading = false;
        alert("Unable to create a line of treatment");
        deferred.resolve();
      });

      return deferred.promise;
    };

    this.delete = function(episode){
      if(self.readonly){
        return;
      }
      var deferred = $q.defer();
      var deleteModal =  $modal.open({
          templateUrl: '/templates/delete_lot_modal.html',
          controller: 'DeleteLOTConfirmationCtrl',
          resolve: {
              episode: function() {
                  return episode;
              }
          }
      });
      deleteModal.result.then(function(result){
        if(result === "deleted"){
          $scope.refresh().then(deferred.resolve());
        }
        else{
          deferred.resolve();
        }
      });
    };

    this.lineOfTreatmentOrder = function(lot){
      /*
      * Orders the line of treatments in the patient detail page
      * by the earliest regimen date of that episode.
      */
      var regimens = _.sortBy(EntrytoolHelper.getEpisodeRegimen(lot), function(regimen){
        return regimen.start_date
      });
      if(!regimens.length){
        // if there are no regimens attatched to the lot we
        // we want it to show at the top of the regimens
        // so return a date far in the future
        return toMomentFilter(new Date(3000, 1, 1));
      }
      return regimens[0].start_date;
    };
  }
);
