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
	return {
		demographics: {
			hospital_number: {
				errors: [
					[Validators.required, "{% trans "External identifier is required" %}"],
					[Validators.maxLength(255), "{% trans "Maximum length is 255" %}"]
				]
			},
			sex: {
				errors: [
					[Validators.required, "{% trans "Sex is required" %}"]
				]
			}
		},
		patient_status: {
			death_date: {
				errors: [
					[Validators.afterDateOfBirth,  "{% trans "Date of death is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of death cannot be in the future" %}"]
				]
			}
		},

		// CLL Condition
		cll_diagnosis_details: {
			diag_date: {
				errors: [
					[Validators.requiredForCategory('CLL'), "{% trans "Diagnosis date is required" %}"],
					[Validators.validateDateOfDiagnosisAgainstRegimen, "{% trans "Date of diagnosis is after a regimen start date" %}"],
					[Validators.validateDateOfDiagnosisAgainstResponse, "{% trans "Date of diagnosis is after a response date" %}"],
					[Validators.validateDateOfDiagnosisAgainstSCT, "{% trans "Date of diagnosis is after the date of a stem cell transplant " %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of diagnosis cannot be in the future" %}"]
				]
			},
			binet_stage: {
				errors: [
					[Validators.requiredForCategory('CLL'), "{% trans "Binet stage is required" %}"]
				]
			}
		},
		cll_regimen: {
			regimen: {
				errors: [
					[Validators.regimenRequiredForCLL, "{% trans "Regimen is required" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
		},
		best_response: {
			response_date: {
				errors: [
					[Validators.required, "{% trans "The response date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "The response date should be after the date of diagnosis" %}"],
					[Validators.noFuture, "{% trans "The response date is in the future" %}"],
				]
			},
			response: {
				response: {
					errors: [
						[Validators.required, "{% trans "Response is required" %}"],
					]
				}
			}
		},
		additional_characteristics: {
			characteristic_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
					[Validators.required, "{% trans "Date is required" %}"]
				]
			},
			cirs_score: {
				errors: [
					[Validators.lessThan(56), "{% trans "CIRS is too high" %}"],
					[Validators.greaterThan(0), "{% trans "CIRS is too low" %}"],
				],
			},
			creatinine_clearance: {
				errors: [
					[Validators.greaterThan(0), "{% trans "Creatinine clearance is too low" %}"],
				]
			},
			LDH: {
				errors: [
					[Validators.greaterThan(0), "{% trans "LDH is too low" %}"],
				]
			},
			beta2m: {
				errors: [
					[Validators.greaterThan(0), "{% trans "Beta-2-Microglobulin is too low" %}"],
				],
				warnings: [
					[Validators.lessThan(25), "{% trans "Beta-2-Microglobulin is too low" %}"],
				]
			},
		},
		cytogenetics: {
			cytogenetic_date: {
				errors: [
					[Validators.required, "{% trans "Date is required" %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
				]
			}
		},
		quality_of_life5q: {
			q5_date: {
				errors: [
					[Validators.required, "{% trans "Date is required" %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
				]
			}
		},
		sct: {
			sct_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate, "{% trans "The SCT should be after the date of diagnosis" %}"]
				]
			}
		},

		// MM Condition
		mm_diagnosis_details: {
			diag_date: {
				errors: [
					[Validators.requiredForCategory('MM'), "{% trans "Diagnosis date is required" %}"],
					[Validators.validateDateOfDiagnosisAgainstRegimen, "{% trans "Date of diagnosis is after a regimen start date" %}"],
					[Validators.validateDateOfDiagnosisAgainstResponse, "{% trans "Date of diagnosis is after a response date" %}"],
					[Validators.validateDateOfDiagnosisAgainstSCT, "{% trans "Date of diagnosis is after the date of a stem cell transplant " %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of diagnosis cannot be in the future" %}"]
				]
			},
			smm_history: {
				errors: [
					[Validators.requiredForCategory('MM'), "{% trans "History of SMM is required" %}"],
				]
			},
			smm_history_date: {
				errors: [
					[Validators.requiredIfSMM, "{% trans "Date is required" %}"],
					[Validators.sameOrBeforeDiagnosisDate, "{% trans "Date must be before the date of diagnosis" %}"],
				]
			}
		},
		mm_regimen: {
			regimen: {
				errors: [
					[Validators.regimenRequiredForMM, "{% trans "Regimen is required" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.validateRegimenDateBetween, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenSurrounds, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
		},
		mm_response: {
			response_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate,  "{% trans "The response should be after the date of diagnosis" %}"],
					[Validators.required,  "{% trans "The response date is required" %}"],
					[Validators.noFuture, "{% trans "The response date is in the future" %}"]
				],
				warnings: [
					[Validators.validateResponseToRegimens,  "{% trans "No regimen is connected to this response" %}"]
				]
			},
			response: {
				errors: [
					[Validators.required, "{% trans "Response is required" %}"],
				]
			}
		},
		mm_follow_up: {
			follow_up_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Visit date must be after the date of birth" %}"],
					[Validators.required, "{% trans "Visit date is required" %}"],
				]
			},
			hospital: {
				errors: [
					[Validators.required, "{% trans "Hospital is required" %}"]
				]
			},
			LDH: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "LDH is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "LDH is too high" %}"],
				],
				warnings: [
					[Validators.greaterThan(10),  "{% trans "LDH is too low" %}"],
					[Validators.lessThan(50),  "{% trans "LDH is too high" %}"],
				]
			},
			beta2m: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "beta2m is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "beta2m is too high" %}"],
				],
			},
			albumin: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "Albumin is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "Albumin is too high" %}"],
				],
			},
			mprotein_serum: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "MProtein Serum is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "MProtein Serum is too high" %}"],
				],
			},
			mprotein_urine: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "MProtein Urine is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "MProtein Urine is too high" %}"],
				],
			},
			mprotein_24h: {
				errors: [
					[Validators.greaterThan(0),  "{% trans "Mprotein in 24 hour urine is too low" %}"],
					[Validators.lessThan(1000),  "{% trans "Mprotein in 24 hour urine is too high" %}"],
				],
			},
		}
	}
});
