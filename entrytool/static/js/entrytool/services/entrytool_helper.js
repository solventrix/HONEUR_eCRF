angular.module('opal.services').factory('EntrytoolHelper', function() {
	return {
		getDiagnosis: function(patient){
			/*
			* Different conditions have different diagnosis models.
			* these are not on the LOT episode category but on
			* the condition episode category.
			*
			* A patient should only have a single episode category so
			* we iterate over the patients episodes until we
			* find a diagnosis that has been populated (has a consistency token)
			* and return that.
			*
			* Diagnosis is a singleton so we return the object rather than
			* an array of obects.
			*/
			var result = null;

			_.each(patient.episodes, function(episode){
				if(episode.cll_diagnosis_details[0].consistency_token){
					result = episode.cll_diagnosis_details[0]
				}
				else if(episode.mm_diagnosis_details[0].consistency_token){
					result = episode.mm_diagnosis_details[0]
				}
			});
			return result;
		},

		getEpisodeRegimen: function(episode){
			/*
			* Different conditions have diferently named regimen but all
			* have the same underlying date fields, used for validation.
			*
			* This returns the regimen, no matter what the condition is
			*/
			if(episode.cll_regimen.length){
				return episode.cll_regimen
			}
			return episode.mm_regimen
		},

		getEpisodeResponse: function(episode){
			/*
			* Different conditions have diferently named responses but all
			* have the same underlying date fields, used for validation.
			*
			* This returns the responses, no matter what the condition is
			*/
			if(episode.best_response.length){
				return episode.best_response
			}
			return episode.mm_response
		}
	}

})
