{% load i18n %}
angular.module('opal.services').service('ValidationRules', function(Validators) {
	"use strict";
	/*
	* Should return an object that looks like
	{
		modelApiName: {
			fieldName: {
				errors: [
					[someValidationFunction, {% trans "Error message to show if validationFunction returns true" %}]
				]
				warnings: [
					[someValidationFunction, {% trans "Warning message to show if validationFunction returns true" %}]
				]
			}
		}
	}
	*/
	return {}
});
