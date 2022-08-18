directives.directive("formSubmit", function($http){
  return {
    scope: {
			callBack: '&callBack',
		},
    link: function(scope, element, attrs){
			"use strict";
			/*
			* Submits a single file field to the {url} in the request
			* dictionary with a {formfield} and then calls the {callBack}
			*/
			$(element).on('submit', function(){
				var formData = new FormData();
				formData.append(attrs.formField, $($(element).find('input')[0]).prop('files')[0]);
				$http({
					url: attrs.url,
					method: "POST",
					data: formData,
					headers: {'Content-Type': "application/zip"}
				}).then(function(response){
					scope.callBack()(response);
				});

			})

    }
  };
});
