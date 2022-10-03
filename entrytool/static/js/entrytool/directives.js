directives.directive("formSubmit", function($http){
  return {
    scope: {
			onSubmit: '&onSubmit',
			onSuccess: '&onSuccess',
			onFail: '&onFail',
		},
    link: function(scope, element, attrs){
			"use strict";
			/*
			* Submits a single file field to the {url} in the request
			* dictionary with a {formfield} and then calls the {callBack}
			*/

			// this is the attribute shown as the 'placeholder' in our faux
			// form button
			var fauxField = $(element).find('#faux-file-field');
			var input = $(element).find('input');

			var init = function(){
				input.val(null);
				$(element).removeClass('error');
				fauxField.attr('data-content', fauxField.attr('data-initial-content'));
			}

			input.on('change', function(){
				$(element).removeClass('error');
				var file = $(this).prop('files')[0];
				$('#faux-file-field').attr('data-content', file.name);
			});

			$(element).on('submit', function(){
				scope.onSubmit()();
				var formData = new FormData();
				var file = $($(element).find('input')[0]).prop('files')[0]
				if(!file){
					$(element).addClass('error');
					return;
				}
				formData.append('file', file);
				$http({
					url: attrs.url,
					headers: {
						'Content-Disposition': "attachment; filename=" + file.name,
						'Content-Type': undefined
					},
					method: "POST",
					data: formData,
				}).then(function(response){
						init();
						scope.onSuccess()(response);
				}, function(err){
					  scope.onFail()(err);
				});
			});

			init();
    }
  };
});
