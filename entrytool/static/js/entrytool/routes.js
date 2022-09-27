(function(){
  var app = angular.module('opal');
  app.controller('WelcomeCtrl', function(){});

  app.config(
      ['$routeProvider',
       function($routeProvider){
  //	     $routeProvider.when('/',  {redirectTo: '/list'})

           $routeProvider.when('/',  {
               controller: 'WelcomeCtrl',
               templateUrl: '/templates/welcome.html'}
                              )
          $routeProvider.when('/#/patient',  {
            controller: 'AddEpisodeCtrl'}
                            )

          $routeProvider.when('/data_upload', {
            controller: 'DataUploader',
            templateUrl: '/templates/data_upload.html',
            resolve: {
              unValidatedPatients: function(DataUploadLoader){
                return DataUploadLoader.unValidatedPatients()
              },
              patientsWithErrors: function(DataUploadLoader){
                return DataUploadLoader.patientsWithErrors()
              }
            }
          })
          $routeProvider.when('/lost_to_followup',  {
            controller: 'EmptyCtrl',
            templateUrl: function(params){
            params["cache_bust"] = Date.now();
            return '/lost_to_followup/' + '?' + $.param(params);
            }
          })
       }]);
})();
