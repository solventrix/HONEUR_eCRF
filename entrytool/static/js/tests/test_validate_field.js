describe("ValidatorField", function () {
  "use strict";

	var ValidationRules, ValidateField;

	describe('validate', function(){
		it("should return a {warnings: message} if a validator for a field.warning returns true", function(){
			ValidationRules = {
				diagnosis: {
					diag_date: {
						warnings: [
							[function(){ return true }, "warning"]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate("diagnosis", "diag_date");
			var expected = {"warnings": ["warning"], "errors": []};
			expect(result).toEqual(expected);
		});

		it("should return a {errors: message} if a validator for a field.error returns a true", function(){
			ValidationRules = {
				diagnosis: {
					diag_date: {
						errors: [
							[function(){ return true }, "errors"]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate("diagnosis", "diag_date");
			var expected = {"warnings": [], "errors": ["errors"]};
			expect(result).toEqual(expected);
		});

		it("should return a result with empty arrays if the field does not exist", function(){
			ValidationRules = {
				diagnosis: {
					diag_date: {
						errors: [
							[function(){ return true }, "errors"]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate("diagnosis", "diagnosis");
			var expected = {"warnings": [], "errors": []};
			expect(result).toEqual(expected);
		});

		it("should return a result with empty arrays if the model api name does not exist", function(){
			ValidationRules = {
				diagnosis: {
					diag_date: {
						errors: [
							[function(){ return true }, "errors"]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate("regimen", "start_date");
			var expected = {"warnings": [], "errors": []};
			expect(result).toEqual(expected);
		});

		it("should return a result with empty arrays if validators for an alert type return false", function(){
			ValidationRules = {
				diagnosis: {
					diag_date: {
						errors: [
							[function(){ return false }, "errors"]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate("diagnosis", "diag_date");
			var expected = {"warnings": [], "errors": []};
			expect(result).toEqual(expected);
		});

		it("should pass in the value, instance, episode and patient", function(){
			var valuePassedIn = false;
			var instancePassedIn = false;
			var episodePassedIn = false;
			var patientPassedIn = false;
			ValidationRules = {
				diagnosis: {
					diag_date: {
						errors: [
							[
								function(value, instance, episode, patient){
									valuePassedIn = value === "value";
									instancePassedIn = instance === "instance";
									episodePassedIn = episode === "episode";
									patientPassedIn = patient === "patient";
									return false;
								}, "errors"
							]
						]
					}
				}
			}
			module('opal.services', function($provide){
				$provide.service('ValidationRules', function(){ return ValidationRules});
			});
			inject(function($injector) {
				ValidateField = $injector.get('ValidateField');
			});
			var result = ValidateField.validate(
				"diagnosis", "diag_date", "value", "instance", "episode", "patient"
			);
			var expected = {"warnings": [], "errors": []};
			expect(result).toEqual(expected);
			expect(valuePassedIn).toBe(true);
			expect(instancePassedIn).toBe(true);
			expect(episodePassedIn).toBe(true);
			expect(patientPassedIn).toBe(true);
		})
	})


});
