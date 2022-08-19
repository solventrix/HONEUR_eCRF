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
				var file = $($(element).find('input')[0]).prop('files')[0]
				formData.append('file', file);
				$http({
					url: attrs.url,
					headers: {
						'Content-Disposition': "attachment; filename=" + file.name
					},
					method: "POST",
					data: formData,
					// headers: {'Content-Type': "multipart/form-data"}
				}).then(function(response){
					scope.callBack()(response);
				});

			})

    }
  };
});
