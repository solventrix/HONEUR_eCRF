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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
			status: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},

		// CLL Condition
		cll_diagnosis_details: {
			hospital: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			diag_date: {
				errors: [
					[Validators.requiredForCategory('CLL'), "{% trans "Diagnosis date is required" %}"],
					[Validators.dateOfDiagnosisAgainstRegimen, "{% trans "Date of diagnosis is after a regimen start date" %}"],
					[Validators.dateOfDiagnosisAgainstResponse, "{% trans "Date of diagnosis is after a response date" %}"],
					[Validators.dateOfDiagnosisAgainstSCT, "{% trans "Date of diagnosis is after the date of a stem cell transplant " %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of diagnosis cannot be in the future" %}"]
				]
			},
			binet_stage: {
				errors: [
					[Validators.requiredForCategory('CLL'), "{% trans "Binet stage is required" %}"],
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},
		cll_regimen: {
			category: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			hospital: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			regimen: {
				errors: [
					[Validators.CLLRegimenRequired, "{% trans "Regimen is required" %}"],
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.notBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.regimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.regimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.notBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.regimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.onlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.regimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			stop_reason: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				],
			},
			ighv_rearrangement: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				],
			},
			del11q: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				],
			},
			tp53_mutation: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				],
			},
			karyotype: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_selfcare: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_usual_activities: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_pain_discomfort: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			q5_anxiety_depression: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		sct: {
			sct_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate, "{% trans "The SCT should be after the date of diagnosis" %}"],
					[Validators.required, "{% trans "Date is required" %}"]
				]
			},
			sct_type: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			relation: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			alotph_source: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			tandem_astp: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			atsp_conditioning: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},

		// MM Condition
		mm_diagnosis_details: {
			diag_date: {
				errors: [
					[Validators.requiredForCategory('MM'), "{% trans "Diagnosis date is required" %}"],
					[Validators.dateOfDiagnosisAgainstRegimen, "{% trans "Date of diagnosis is after a regimen start date" %}"],
					[Validators.dateOfDiagnosisAgainstResponse, "{% trans "Date of diagnosis is after a response date" %}"],
					[Validators.dateOfDiagnosisAgainstSCT, "{% trans "Date of diagnosis is after the date of a stem cell transplant " %}"],
					[Validators.afterDateOfBirth, "{% trans "Date of diagnosis is before the date of birth" %}"],
					[Validators.noFuture, "{% trans "Date of diagnosis cannot be in the future" %}"]
				]
			},
			date_of_first_centre_visit: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Visit date must be after the date of birth" %}"],
				]
			},
			diagnosis: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			heavy_chain_type: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			light_chain_type: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			ecog: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			epidemiological_register: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			gah_score: {
				errors: [
					[Validators.lessThanOrEqualTo(94), "{% trans "GAH is too high" %}"],
					[Validators.greaterThanOrEqualTo(0), "{% trans "GAH is too low" %}"],
				]
			},
			imwg_scale: {
				errors: [
					[Validators.lessThanOrEqualTo(8), "{% trans "IMWG is too high" %}"],
					[Validators.greaterThanOrEqualTo(1), "{% trans "IMWG is too low" %}"],
				]
			},
			icc_scale: {
				errors: [
					[Validators.lessThanOrEqualTo(31), "{% trans "ICC is too high" %}"],
					[Validators.greaterThanOrEqualTo(0), "{% trans "ICC is too low" %}"],
				]
			},
		},
		mm_patient_status: {
			status: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			cause_of_death: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		mm_past_medical_history: {
			previous_neoplasm: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			previous_neoplasm_date_of_diagnosis: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date must be after the date of birth" %}"],
				]
			},
			chronic_renal_insufficiency: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			chronic_renal_insufficiency_diagnosis_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date must be after the date of birth" %}"],
				]
			},
			monoclonal_pathology_of_uncertain_meaning: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			monoclonal_pathology_of_uncertain_meaning_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date must be after the date of birth" %}"],
				]
			},
			symtomatic_multiple_myeloma: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			asymtomatic_multiple_myeloma: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			external_pasmocytoma: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		mm_regimen: {
			hospital: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			category: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			regimen: {
				errors: [
					[Validators.requiredIfRegimenTypeNotWatchAndWait, "{% trans "Regimen is required" %}"],
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
					[Validators.sameOrAfterDiagnosisDate, "{% trans "Start Date must be after the patient date of diagnosiss" %}"],
					[Validators.notBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.regimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "The end date should be after the start date" %}"],
				],
				warnings: [
					[Validators.regimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			end_date: {
				errors: [
					[Validators.notBetweenRegimenDates, "{% trans "The regimen cannot overlap with another regimen" %}"],
					[Validators.regimenToOtherLOTRegimens,  "{% trans "This regimen overlaps with another line of treatment" %}"],
					[Validators.endDateSameOrAfterRegimenStartDate, "{% trans "End Date must be after the start date" %}"],
					[Validators.onlyOneOpenRegimen, "{% trans "There can only be one open regimen at a time" %}"]
				],
				warnings: [
					[Validators.regimenToResponses, "{% trans "A response date is not connected to a regimen" %}"]
				]
			},
			stop_reason: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			}
		},
		mm_response: {
			progression_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate,  "{% trans "The progression date should be after the date of diagnosis" %}"],
				]
			},
			response_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate,  "{% trans "The response date should be after the date of diagnosis" %}"],
					[Validators.required,  "{% trans "The response date is required" %}"],
					[Validators.noFuture, "{% trans "The response date is in the future" %}"]
				],
				warnings: [
					[Validators.responseToRegimens,  "{% trans "No regimen is connected to this response" %}"]
				]
			},
			response: {
				errors: [
					[Validators.required, "{% trans "Response is required" %}"],
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			negative_mrd: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			negative_mrd_date: {
				errors: [
					[Validators.sameOrAfterDiagnosisDate,  "{% trans "The negative MRD date should be after the date of diagnosis" %}"],
				]
			},
			mrd_technique: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
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
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
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
		},
		bone_disease: {
			treatment_type: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			start_date: {
				errors: [
					[Validators.required, "{% trans "Start date is required" %}"],
				]
			},
			end_date: {
				errors: [
					[Validators.endDateSameOrAfterBoneDiseaseStartDate, "{% trans "End Date must be after the start date" %}"],
				]
			}
		},
		comorbidity: {
			condition: {
				errors: [
					[Validators.uniqueCondition, "{% trans "A line of treatment cannot have multiple comorbidities of the same type" %}"]
				]
			}
		},
		radiotherapy_induction: {
			start_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Start date must be after the date of birth" %}"],
				]
			},
			end_date: {
				errors: [
					[Validators.endDateSameOrAfterRadioTherapyStartDate, "{% trans "End Date must be after the start date" %}"],
				]
			},
		},
		lab_test: {
			date: {
				errors: [
					[Validators.required, "{% trans "Date is required" %}"],
					[Validators.afterDateOfBirth, "{% trans "Date must be after the date of birth" %}"],
				]
			},
			glomerular_filtration_formula: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			glomerular_filtration_formula_date: {
				errors: [
					[Validators.afterDateOfBirth, "{% trans "Date must be after the date of birth" %}"],
				]
			}
		},
		clinical_presentation: {
			infection_type: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			renal_failure: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			hypercalcemia: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			fever: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			anemia: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			dialysis: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			bone_pain: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			extramedullary_plasmacytomas: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			iss: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			riss: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		imaging: {
			bone_series_test_image: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			ct_scan: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			resonance: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			pet_scan: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			other_imaging_test: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		},
		cytogenetics: {
			t4_14: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t4_14_not_effected: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t4_14_haploid_karyotype: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t4_14_16: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			t11_14: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			del1p: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			del_17p: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			gan1q: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			chromosome_alterations: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			normal_study: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
			other_study: {
				errors: [
					[Validators.inOptions, "{% trans "is not in the options available" %}"]
				]
			},
		}
	}
});
