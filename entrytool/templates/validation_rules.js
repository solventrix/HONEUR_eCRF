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
					[Validators.required, "{% trans "Sex is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},
		patient_status: {
			death_date: {
				errors: [
					[Validators.afterDateOfBirth,  "{% trans "Date of death is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of death cannot be in the future" %}"]
				]
			},
			death_cause: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},

		// CLL Condition
		cll_diagnosis_details: {
			hospital: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
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
					[Validators.requiredForCategory('CLL'), "{% trans "Binet stage is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},
		cll_regimen: {
			category: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			hospital: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			regimen: {
				errors: [
					[Validators.requiredForCategory('CLL'), "{% trans "Regimen is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.validateNotBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.validateNotBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			stop_reason: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
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
				errors: [
					[Validators.required, "{% trans "Response is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},
		additional_characteristics: {
			characteristic_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
					[Validators.required, "{% trans "Date is required" %}"]
				]
			},
			ecog_score: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
			cirs_score: {
				errors: [
					[Validators.lessThanOrEqualTo(56), "{% trans "CIRS is too high" %}"],
					[Validators.greaterThanOrEqualTo(0), "{% trans "CIRS is too low" %}"],
				],
			},
			creatinine_clearance: {
				errors: [
					[Validators.greaterThanOrEqualTo(0), "{% trans "Creatinine clearance is too low" %}"],
				]
			},
			LDH: {
				errors: [
					[Validators.greaterThanOrEqualTo(0), "{% trans "LDH is too low" %}"],
				]
			},
			beta2m: {
				errors: [
					[Validators.greaterThanOrEqualTo(0), "{% trans "Beta-2-Microglobulin is too low" %}"],
				],
				warnings: [
					[Validators.lessThanOrEqualTo(25), "{% trans "Beta-2-Microglobulin is too low" %}"],
				]
			},
			bulky_disease: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			}
		},
		cytogenetics: {
			cytogenetic_date: {
				errors: [
					[Validators.required, "{% trans "Date is required" %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
				]
			},
			del17p: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
			ighv_rearrangement: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
			del11q: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
			tp53_mutation: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
			karyotype: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				],
			},
		},
		quality_of_life5q: {
			q5_date: {
				errors: [
					[Validators.required, "{% trans "Date is required" %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of measurement must be after date of birth" %}"],
				]
			},
			q5_mobility: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_selfcare: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_usual_activities: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_pain_discomfort: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_anxiety_depression: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		sct: {
			sct_type: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			hospital: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
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
			gah_score: {
				errors: [
					[Validators.greaterThanOrEqualTo(0), "{% trans "GAH Score is too low" %}"],
					[Validators.lessThanOrEqualTo(94), "{% trans "GAH Score is too high" %}"],
				]
			},
			imwg_scale: {
				errors: [
					[Validators.greaterThanOrEqualTo(1), "{% trans "IMWG Scale is too low" %}"],
					[Validators.lessThanOrEqualTo(8), "{% trans "IMWG Scale is too high" %}"],
				]
			},
			icc_scale: {
				errors: [
					[Validators.greaterThanOrEqualTo(0), "{% trans "ICC Scale is too low" %}"],
					[Validators.lessThanOrEqualTo(31), "{% trans "ICC Scale is too low" %}"],
				]
			},
			smm_history: {
				errors: [
					[Validators.requiredForCategory('MM'), "{% trans "History of SMM is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			smm_history_date: {
				errors: [
					[Validators.requiredIfSMM, "{% trans "Date is required" %}"],
					[Validators.sameOrBeforeDiagnosisDate, "{% trans "Date must be before the date of diagnosis" %}"],
				]
			},
			mgus_history: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			iss_stage: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			ds_stage: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			pp_type: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			del_17p: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			del_13: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t4_14: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t4_16: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		mm_regimen: {
			hospital: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			regimen: {
				errors: [
					[Validators.requiredForCategory('MM'), "{% trans "Regimen is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			category: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.validateNotBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.validateNotBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.validateRegimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.validateOnlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.validateRegimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			stop_reason: {
				errors: [
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			}
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
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.required, "{% trans "Hospital is required" %}"],
					[Validators.validateInOptions, "{% trans "is not in the options available" %}"]
				]
			},
			LDH: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "LDH is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "LDH is too high" %}"],
				],
				warnings: [
					[Validators.greaterThanOrEqualTo(10),  "{% trans "LDH is too low" %}"],
					[Validators.lessThanOrEqualTo(50),  "{% trans "LDH is too high" %}"],
				]
			},
			beta2m: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "beta2m is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "beta2m is too high" %}"],
				],
			},
			albumin: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "Albumin is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "Albumin is too high" %}"],
				],
			},
			mprotein_serum: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "MProtein Serum is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "MProtein Serum is too high" %}"],
				],
			},
			mprotein_urine: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "MProtein Urine is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "MProtein Urine is too high" %}"],
				],
			},
			mprotein_24h: {
				errors: [
					[Validators.greaterThanOrEqualTo(0),  "{% trans "Mprotein in 24 hour urine is too low" %}"],
					[Validators.lessThanOrEqualTo(1000),  "{% trans "Mprotein in 24 hour urine is too high" %}"],
				],
			},
		}
	}
});
