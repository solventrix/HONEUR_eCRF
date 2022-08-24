describe("Validators", function () {
  "use strict";
	var Validators, EntrytoolHelper;
	var today, yesterday, two_days_ago;
	var patient, episode, last_week, two_weeks_ago;
	beforeEach(function () {
    module("opal.services");
    module("opal.filters");
  });

	beforeEach(function () {
    inject(function ($injector) {
			Validators = $injector.get("Validators");
			EntrytoolHelper = $injector.get("EntrytoolHelper");
    });
		today = moment()
		two_days_ago = moment().subtract(2, "d");
		yesterday = moment().subtract(1, "d");
		last_week = moment().subtract(7, "d");
		two_weeks_ago = moment().subtract(14, "d");
		patient = {};
		episode = {}
	});

	describe('dateOfDiagnosisAgainstRegimen', function(){
		it("should return true if the date of diagnosis is falsy", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_days_ago}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(null, null, null, patient)).toBe(true);
		});

		it("should return true if the date of diagnosis is before the regimen start date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: yesterday}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true there are no regimen", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true there is a regiment but it has no start date or end date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true if it is the same day as a regimen", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: yesterday}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(yesterday, null, null, patient)).toBe(true);
		});

		it("should return false if there is a regimen before the date of diagnosis", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_days_ago}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(yesterday, null, null, patient)).toBe(false);
		});

		it('should return false if there is no start date but the end date is before', function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{end_date: two_days_ago}]);
			expect(Validators.dateOfDiagnosisAgainstRegimen(yesterday, null, null, patient)).toBe(false);
		});
	});

	describe('dateOfDiagnosisAgainstResponse', function(){
		it("should return true if the date of diagnosis is falsy", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: two_days_ago}]);
			expect(Validators.dateOfDiagnosisAgainstResponse(null, null, null, patient)).toBe(true);
		});

		it("should return true if the date of diagnosis is before the response date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: yesterday}]);
			expect(Validators.dateOfDiagnosisAgainstResponse(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true there are no responses", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([]);
			expect(Validators.dateOfDiagnosisAgainstResponse(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true there is not response date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: null}]);
			expect(Validators.dateOfDiagnosisAgainstResponse(two_days_ago, null, null, patient)).toBe(true);
		});


		it("should return true if it is the same day as a response", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: yesterday}]);
			expect(Validators.dateOfDiagnosisAgainstResponse(yesterday, null, null, patient)).toBe(true);
		});

		it("should return false if there is a response before the date of diagnosis", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: two_days_ago}]);
			expect(Validators.dateOfDiagnosisAgainstResponse(yesterday, null, null, patient)).toBe(false);
		});
	});

	describe('dateOfDiagnosisAgainstSCT', function(){
		it("should return true if the date of diagnosis is falsy", function(){
			patient.episodes = [episode]
			episode.sct = [{sct_date: two_days_ago}]
			expect(Validators.dateOfDiagnosisAgainstSCT(null, null, null, patient)).toBe(true);
		});

		it("should return true if the date of diagnosis is before the SCT date", function(){
			patient.episodes = [episode]
			episode.sct = [{sct_date: yesterday}]
			expect(Validators.dateOfDiagnosisAgainstSCT(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true there are no SCTs", function(){
			patient.episodes = [episode]
			episode.sct = []
			expect(Validators.dateOfDiagnosisAgainstSCT(two_days_ago, null, null, patient)).toBe(true);
		});

		it("should return true if it is the same day as an SCT", function(){
			patient.episodes = [episode]
			episode.sct = [{sct_date: yesterday}]
			expect(Validators.dateOfDiagnosisAgainstSCT(yesterday, null, null, patient)).toBe(true);
		});

		it("should return false if there is an SCT before the date of diagnosis", function(){
			patient.episodes = [episode]
			episode.sct = [{sct_date: two_days_ago}]
			expect(Validators.dateOfDiagnosisAgainstSCT(yesterday, null, null, patient)).toBe(false);
		});
	});

	describe('notBetweenRegimenDates', function(){
		var regimen = {};
		var instance = {};
		beforeEach(function () {
			regimen.start_date = last_week;
			regimen.end_date = two_days_ago;
			regimen.id = 2;
			instance.id = null;
		});

		it("should return true if the input is not within the start/end", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			expect(Validators.notBetweenRegimenDates(yesterday, instance, null, patient)).toBe(true);
		});

		it("should return true there are no regimen", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([]);
			expect(Validators.notBetweenRegimenDates(yesterday, instance, null, patient)).toBe(true);
		});

		it("should return true if there is no regimen with an end date", function(){
			regimen.end_date = null;
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			expect(Validators.notBetweenRegimenDates(yesterday, instance, null, patient)).toBe(true);
		});

		it('should return true if the instance is the regimen we are talking about', function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			instance.id = 2;
			expect(Validators.notBetweenRegimenDates(last_week, instance, null, patient)).toBe(true);
		})

		it("should return false if the date matches a regimen start date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			expect(Validators.notBetweenRegimenDates(last_week, instance, null, patient)).toBe(false);
		});

		it("should return false if the date matches a regimen end date", function(){
			patient.episodes = [episode]
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			expect(Validators.notBetweenRegimenDates(two_days_ago, instance, null, patient)).toBe(false);
		});

		it("should return false if the date is between the start and the end date", function(){
			patient.episodes = [episode]
			regimen.end_date = yesterday;
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen]);
			expect(Validators.notBetweenRegimenDates(two_days_ago, instance, null, patient)).toBe(false);
		});
	});

	describe('onlyOneOpenRegimen', function(){
		it("should return true if the instance has an end date", function(){
			patient.episodes = [
				{
					id: 1,
				},
				{
					id: 2
				}
			]

			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_weeks_ago, id: 1}]);

			expect(Validators.onlyOneOpenRegimen(two_days_ago, {id: 2}, null, patient)).toBe(true);
		});

		it("should return true if it is the only regimen", function(){
			patient.episodes = [
				{
					id: 1,
				},
				{
					id: 2
				}
			]

			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([]);

			expect(Validators.onlyOneOpenRegimen([null, {start_date: two_weeks_ago}], null, patient)).toBe(true);
		});

		it("should return true if it is there is another regimen that is closed", function(){
			patient.episodes = [
				{
					id: 1,
				},
			]

			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_weeks_ago, end_date: two_days_ago, id:2}]);

			expect(Validators.onlyOneOpenRegimen(null, {id: 1}, null, patient)).toBe(true);
		});

		it("should return true if the other open regimen is the regimen pass in", function(){
			patient.episodes = [
				{
					id: 1,
				},
			]

			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_weeks_ago, id:2}]);

			expect(Validators.onlyOneOpenRegimen(null, {id: 2}, null, patient)).toBe(true);
		});

		it("should return false if there is another open regimen", function(){
			patient.episodes = [
				{
					id: 1,
				},
			]

			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([{start_date: two_weeks_ago, id:1}]);

			expect(Validators.onlyOneOpenRegimen(null, {id: 2}, null, patient)).toBe(false);
		});
	});

	describe('regimenToOtherLOTRegimens', function(){
		it('should return true if there are no other lot regimen', function(){
			episode.id = 2
			var regimen_1 = {
				id: 1,
				start_date: moment().subtract(22, "d"),
				end_date: moment().subtract(20, "d")
			}
			var regimen_2 = {
				id: 2,
				start_date: moment().subtract(12, "d"),
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValue([regimen_1, regimen_2, regimen_3]);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(true);
		});

		it('should return true if there is another lot regimen but it is not surrounded', function(){
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment().subtract(22, "d"),
				end_date: moment().subtract(20, "d")
			}
			var regimen_2 = {
				id: 2,
				start_date: moment().subtract(12, "d"),
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues(
				[regimen_1, regimen_2],
				[regimen_3]
			);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(true);
		});

		it('should return false if there is another lot regiment that is around this one', function(){
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment().subtract(22, "d"),
				end_date: moment().subtract(20, "d")
			}
			var regimen_2 = {
				id: 2,
				start_date: moment().subtract(12, "d"),
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues([regimen_2], [regimen_1, regimen_3]);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(false);
		});

		it('should return false if there is an overlap at the start', function(){
				// e.g.
				// this episode min 1 Jul, max 5 Jul should return an error
				// other episode min 3 Jul, other episode Max 10 Jul
				episode.id = 2
				var episode_2 = {
					id: 3
				}
				var regimen_1 = {
					id: 1,
					start_date: moment("01-07-2020", "DD-MM-YYYY"),
					end_date: moment("05-07-2020", "DD-MM-YYYY")
				}
				var regimen_2 = {
					id: 3,
					start_date: moment("03-07-2020", "DD-MM-YYYY"),
					end_date: moment("04-07-2020", "DD-MM-YYYY")
				}
				var regimen_3 = {
					id: 2,
					start_date: moment("09-07-2020", "DD-MM-YYYY"),
					end_date: moment("10-07-2020", "DD-MM-YYYY")
				}
				patient.episodes = [episode, episode_2];
				spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues([regimen_1], [regimen_2, regimen_3]);
				expect(Validators.regimenToOtherLOTRegimens(regimen_1.start_date, regimen_1, episode, patient)).toBe(false);
		});

		it('should return false if there is an overlap at the end', function(){
			// e.g.
			// this episode 8 Jul, max 12 Jul
			// other episode min 3 Jul, other episode max 10 Jul
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment("08-07-2020", "DD-MM-YYYY"),
				end_date: moment("10-07-2020", "DD-MM-YYYY")
			}
			var regimen_2 = {
				id: 3,
				start_date: moment("03-07-2020", "DD-MM-YYYY"),
				end_date: moment("04-07-2020", "DD-MM-YYYY")
			}
			var regimen_3 = {
				id: 2,
				start_date: moment("10-07-2020", "DD-MM-YYYY"),
				end_date: moment("11-07-2020", "DD-MM-YYYY")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues([regimen_1], [regimen_2, regimen_3]);
			expect(Validators.regimenToOtherLOTRegimens(regimen_1.start_date, regimen_1, episode, patient)).toBe(false);
		});

		it('should return false if there is a single other episode date in the middle of this episode', function(){
			// e.g.
			// this episode 8 Jul, max 12 Jul
			// other episode min 9 Jul
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment("08-07-2020", "DD-MM-YYYY"),
				end_date: moment("12-07-2020", "DD-MM-YYYY")
			}
			var regimen_2 = {
				id: 3,
				start_date: moment("09-07-2020", "DD-MM-YYYY"),
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues([regimen_1], [regimen_2]);
			expect(Validators.regimenToOtherLOTRegimens(regimen_1.start_date, regimen_1, episode, patient)).toBe(false);
		});

		it('should return false if there is single date on the episode in the middle of another episode', function(){
			// e.g.e
			// this episode 9 Jul
			// other episode 8 Jul, max 12 Jul
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment("09-07-2020", "DD-MM-YYYY"),
			}
			var regimen_2 = {
				id: 3,
				start_date: moment("03-07-2020", "DD-MM-YYYY"),
			}
			var regimen_3 = {
				id: 2,
				start_date: moment("10-07-2020", "DD-MM-YYYY"),
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues([regimen_1], [regimen_2, regimen_3]);
			expect(Validators.regimenToOtherLOTRegimens(regimen_1.start_date, regimen_1, episode, patient)).toBe(false);
		});

		it('should return true if there is only an end date and another episode surrounds it', function(){
			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment().subtract(22, "d"),
				end_date: moment().subtract(20, "d")
			}
			var regimen_2 = {
				id: 2,
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues(
				[regimen_1, regimen_2],
				[regimen_3]
			);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(true);
		});

		it('should return true if there is only an end date on one of the other episodes that surround it', function(){			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				end_date: moment().subtract(20, "d")
			}
			var regimen_2 = {
				id: 2,
				start_date: moment().subtract(12, "d"),
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues(
				[regimen_1, regimen_2],
				[regimen_3]
			);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(true);
		});

		it('should return true if there is only an start date on one of the other episodes that surround it', function(){			episode.id = 2
			var episode_2 = {
				id: 3
			}
			var regimen_1 = {
				id: 1,
				start_date: moment().subtract(22, "d"),
			}
			var regimen_2 = {
				id: 2,
				start_date: moment().subtract(12, "d"),
				end_date: moment().subtract(10, "d")
			}
			var regimen_3 = {
				id: 3,
				start_date: moment().subtract(7, "d"),
				end_date: moment().subtract(5, "d")
			}
			patient.episodes = [episode, episode_2];
			spyOn(EntrytoolHelper, 'getEpisodeRegimen').and.returnValues(
				[regimen_1, regimen_2],
				[regimen_3]
			);
			expect(Validators.regimenToOtherLOTRegimens(regimen_2.start_date, regimen_2, episode, patient)).toBe(true);
		});
	});

	describe("regimenToResponses", function(){
		it("should return true if the value is not populated", function(){
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: moment().subtract(100, "d")}]);
			expect(Validators.regimenToResponses(null, {start_date: two_weeks_ago}, episode)).toBe(true);
		});

		it("should return true if there is no response", function(){
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([]);
			expect(Validators.regimenToResponses(two_weeks_ago, {start_date: two_weeks_ago}, episode)).toBe(true);
		});

		it("should return true if the response date is within 30 days of the value", function(){
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: two_weeks_ago}]);
			expect(Validators.regimenToResponses(two_days_ago, {start_date: two_days_ago}, episode)).toBe(true);
		})

		it("should return false if the response date is greater than 30 days of the value", function(){
			spyOn(EntrytoolHelper, 'getEpisodeResponse').and.returnValue([{response_date: moment().subtract(100, "d")}]);
			expect(Validators.regimenToResponses(two_days_ago, {start_date: two_days_ago}, episode)).toBe(false);
		});
	});



	describe("sameOrAfterDiagnosisDate", function(){
		it("should return true if there is no diagnosis", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues(null);
			expect(Validators.sameOrAfterDiagnosisDate(two_days_ago, null, null, null)).toBe(true);
		});

		it("should return true if there is no diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: null});
			expect(Validators.sameOrAfterDiagnosisDate(two_days_ago, null, null, null)).toBe(true);
		});

		it("should return true if there is no value", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrAfterDiagnosisDate(null, null, null, null)).toBe(true);
		});

		it("should return true if the value is the same as the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrAfterDiagnosisDate(moment().subtract(2, "d"), null, null, null)).toBe(true);
		});

		it("should return true if the value is after the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_weeks_ago});
			expect(Validators.sameOrAfterDiagnosisDate(two_days_ago, null, null, null)).toBe(true);
		});

		it("should return false if the value is before the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrAfterDiagnosisDate(two_weeks_ago, null, null, null)).toBe(false);
		});
	})

	describe("sameOrBeforeDiagnosisDate", function(){
		it("should return true if there is no diagnosis", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues(null);
			expect(Validators.sameOrBeforeDiagnosisDate(two_days_ago, null, null, null)).toBe(true);
		});

		it("should return true if there is no diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: null});
			expect(Validators.sameOrBeforeDiagnosisDate(two_days_ago, null, null, null)).toBe(true);
		});

		it("should return true if there is no value", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrBeforeDiagnosisDate(null, null, null, null)).toBe(true);
		});

		it("should return true if the value is the same as the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrBeforeDiagnosisDate(moment().subtract(2, "d"), null, null, null)).toBe(true);
		});

		it("should return true if the value is before the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_days_ago});
			expect(Validators.sameOrBeforeDiagnosisDate(two_weeks_ago, null, null, null)).toBe(true);
		});

		it("should return false if the value is after the diagnosis date", function(){
			spyOn(EntrytoolHelper, 'getDiagnosis').and.returnValues({diag_date: two_weeks_ago});
			expect(Validators.sameOrBeforeDiagnosisDate(two_days_ago, null, null, null)).toBe(false);
		});
	})

	describe("afterDateOfBirth", function(){
		it("should return true if it is after the date of birth", function(){
			episode.demographics = [{date_of_birth: two_weeks_ago}];
			var value = two_days_ago;
			expect(Validators.afterDateOfBirth(value, null, episode)).toBe(true);
		});

		it("should return true if the value is not populated", function(){
			episode.demographics = [{date_of_birth: two_weeks_ago}];
			var value = null;
			expect(Validators.afterDateOfBirth(value, null, episode)).toBe(true);
		});

		it("should return true if the value is the same as the date of birth", function(){
			episode.demographics = [{date_of_birth: moment().subtract(2, "d")}];
			var value = two_days_ago;
			expect(Validators.afterDateOfBirth(value, null, episode)).toBe(true);
		});

		it("should return false if the value is before the date of birth", function(){
			episode.demographics = [{date_of_birth: two_days_ago}];
			var value = two_weeks_ago;
			expect(Validators.afterDateOfBirth(value, null, episode)).toBe(false);
		});
	});

	describe('endDateSameOrAfterRegimenStartDate', function(){
		it('should return true if the end date is after the start date', function(){
			var regimen = {
				start_date: last_week,
				end_date: two_days_ago
			}

			expect(Validators.endDateSameOrAfterRegimenStartDate(null, regimen)).toBe(true);
		});

		it("should return true if the end date is the same as the start date", function(){
			var regimen = {
				start_date: moment().subtract(2, "d"),
				end_date: two_days_ago
			}

			expect(Validators.endDateSameOrAfterRegimenStartDate(null, regimen)).toBe(true);
		});

		it("should return true if there is no end date", function(){
			var regimen = {
				start_date: two_days_ago
			}

			expect(Validators.endDateSameOrAfterRegimenStartDate(null, regimen)).toBe(true);
		});

		it("should return false if the end date is after the start date", function(){
			var regimen = {
				start_date: two_days_ago,
				end_date: last_week
			}

			expect(Validators.endDateSameOrAfterRegimenStartDate(null, regimen)).toBe(false);
		});
	})


	describe('requiredIfSMM', function(){
		var instance;

		beforeEach(function(){
			instance = {smm_history: "Yes"}
		});

		it('should return true if the value is populated', function(){
			expect(Validators.requiredIfSMM('Yes', instance)).toBe(true);
		});

		it('should return true if the value is 0', function(){
			expect(Validators.requiredIfSMM(0, instance)).toBe(true);
		});

		it('should return true if smm_history is false', function(){
			instance.smm_history = "No";
			expect(Validators.requiredIfSMM(null, instance)).toBe(true);
		});

		it('should return false if the value is null', function(){
			expect(Validators.requiredIfSMM(null, instance)).toBe(false);
		});

		it('should return false if the value is undefined', function(){
			expect(Validators.requiredIfSMM(undefined, instance)).toBe(false);
		});
	});


	describe('required', function(){
		it('should return true if the value is populated', function(){
			expect(Validators.required('Yes')).toBe(true);
		});

		it('should return true if the value is 0', function(){
			expect(Validators.required(0)).toBe(true);
		});

		it('should return false if the value is an empty string', function(){
			expect(Validators.required("")).toBe(false);
		});

		it('should return false if the value is null', function(){
			expect(Validators.required(null)).toBe(false);
		});

		it('should return false if the value is undefined', function(){
			expect(Validators.required(undefined)).toBe(false);
		});
	});

	describe("requiredForCategory", function(){
		it("should return true if the value is populated", function(){
			episode.category = "MM";
			var value = 1;
			expect(Validators.requiredForCategory("MM")(value, null, episode)).toBe(true);
		});

		it("should return true if the value is populated with 0", function(){
			episode.category = "MM";
			var value = 0;
			expect(Validators.requiredForCategory("MM")(value, null, episode)).toBe(true);
		});

		it("should return true if the episode is of a different category", function(){
			episode.category = "CLL";
			var value = null;
			expect(Validators.requiredForCategory("MM")(value, null, episode)).toBe(true);
		});

		it("should return false if the episode is of the category stated and the value is null", function(){
			episode.category_name = "MM";
			var value = null;
			expect(Validators.requiredForCategory("MM")(value, null, episode)).toBe(false);
		});

		it("should return false if the episode is of the category stated and the value is undefined", function(){
			episode.category_name = "MM";
			var value = undefined;
			expect(Validators.requiredForCategory("MM")(value, null, episode)).toBe(false);
		});
	})

	describe("lessThanOrEqualTo", function(){
		it("should return true if the number is not populated", function(){
			expect(Validators.lessThanOrEqualTo(5)(null)).toBe(true);
		});

		it("should return true if the model value is the equal than the constraint", function(){
			expect(Validators.lessThanOrEqualTo(5)(5)).toBe(true);
		});

		it("should return true if the model value is less than the constraint", function(){
			expect(Validators.lessThanOrEqualTo(5)(4)).toBe(true);
		});

		it("should return false if the model value is greater than the constraint", function(){
			expect(Validators.lessThanOrEqualTo(5)(6)).toBe(false);
		});
	});

	describe("greaterThanOrEqualTo", function(){
		it("should return true if the number is not populated", function(){
			expect(Validators.greaterThanOrEqualTo(5)(null)).toBe(true);
		});

		it("should return true if the model value is equal to the constraint", function(){
			expect(Validators.greaterThanOrEqualTo(5)(5)).toBe(true);
		});

		it("should return true if the model value is greater than the constraint", function(){
			expect(Validators.greaterThanOrEqualTo(5)(6)).toBe(true);
		});

		it("should return false if the model value is less than the constraint", function(){
			expect(Validators.greaterThanOrEqualTo(5)(4)).toBe(false);
		});
	});

	describe("maxLength", function(){
		it("should return true if the string is not populated", function(){
			expect(Validators.maxLength(5)(null)).toBe(true);
		});

		it("should return true if the string is the max length", function(){
			expect(Validators.maxLength(5)('fives')).toBe(true);
		});

		it("should return true if the string is less than the max length", function(){
			expect(Validators.maxLength(5)('five')).toBe(true);
		});

		it("should return false if the string is greater than the max length", function(){
			expect(Validators.maxLength(5)('toobig')).toBe(false);
		})
	})


	describe('noFuture', function(){

		it('should return true if the date is not populated', function(){
			expect(Validators.noFuture(null)).toBe(true);
		});

		it("should return true if the date is today", function(){
			expect(Validators.noFuture(moment())).toBe(true);
		});

		it("should return true if the date is yesterday", function(){
			expect(Validators.noFuture(moment().subtract(1, "d"))).toBe(true);
		});

		it("should return false if the date is tomorrow", function(){
			expect(Validators.noFuture(moment().add(1, "d"))).toBe(false);
		})
	});

	describe('inOptions', function(){
		var enum_schema;
		var lookup_list_schema;
		var lookuplists;
		var apiName;
		var fieldName;

		beforeEach(function(){
			apiName = "diagnosis";
			fieldName = "some_test";
			lookup_list_schema = {
				diagnosis: {
					fields: [{
						name: "some_test",
						lookup_list: ["letters"]
					}]
				}
			};
			enum_schema = {
				diagnosis: {
					fields: [{
						name: "some_test",
						enum: ["a", "b", "c"],
					}]
				}
			};
			lookuplists = {
				letters: ["a", "b", "c"]
			};
		});

		it('should return true if the value is not populated', function(){
			expect(Validators.inOptions(
				null, null, null, null, apiName, fieldName, enum_schema, lookuplists
			)).toBe(true);
		});

		it("should return true if the value is in the enum", function(){
			expect(Validators.inOptions(
				"a", null, null, null, apiName, fieldName, enum_schema, lookuplists
			)).toBe(true);
		});

		it("should return true if the value is in the lookuplist", function(){
			expect(Validators.inOptions(
				"a", null, null, null, apiName, fieldName, lookup_list_schema, lookuplists
			)).toBe(true);
		});

		it("should return false if the value is not in the enum", function(){
			expect(Validators.inOptions(
				"d", null, null, null, apiName, fieldName, enum_schema, lookuplists
			)).toBe(false);
		});

		it("should return false if the value is not in the lookuplist", function(){
			expect(Validators.inOptions(
				"d", null, null, null, apiName, fieldName, lookup_list_schema, lookuplists
			)).toBe(false);
		});
	});

	describe('sameOrAfterInstanceField', function(){
		it("should return true if the val isn't populated", function(){
			expect(Validators.sameOrAfterInstanceField('end_date')(null, {end_date: two_days_ago})).toBe(true);
		});

		it("should return true if the instance field isn't populated", function(){
			expect(Validators.sameOrAfterInstanceField('end_date')(two_days_ago, {end_date: null})).toBe(true);
		});

		it("should return true if the val is the same as the instance field", function(){
			expect(Validators.sameOrAfterInstanceField('end_date')(two_days_ago, {end_date: moment(two_days_ago)})).toBe(true);
		});

		it("should return true if the val is after the instance field", function(){
			expect(Validators.sameOrAfterInstanceField('end_date')(two_days_ago, {end_date: two_weeks_ago})).toBe(true);
		});

		it("should return false if the val is before the instance field", function(){
			expect(Validators.sameOrAfterInstanceField('end_date')(two_weeks_ago, {end_date: two_days_ago})).toBe(false);
		});

	})
});
