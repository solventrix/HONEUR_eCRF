describe("PatientValidator", function () {
  "use strict";
  var opalTestHelper, patient, $rootScope, $scope;
  var toMomentFilter, $controller, mockInjector;

  beforeEach(function () {
    module("opal.controllers");
    module("opal.filters");
    module("opal.test");
  });

  beforeEach(function () {
    inject(function ($injector) {
      opalTestHelper = $injector.get("opalTestHelper");
      $rootScope = $injector.get("$rootScope");
      toMomentFilter = $injector.get("toMomentFilter");
      $controller = $injector.get("$controller");
    });
    patient = opalTestHelper.newPatient($rootScope);
    $scope = $rootScope.$new();
    $scope.patient = patient;
    mockInjector = jasmine.createSpyObj(["get"]);

    mockInjector.get.and.returnValue({
      REGIMEN_OVERLAP: "The regimen cannot overlap with another regimen",
      NO_REGIMEN_RESPONSE: "No regimen is connected to this response",
      NO_RESONSE_REGIMEN: "A response date is not connected to a regimen",
      DIAGNOSIS_OVER_REGIMEN_START:
        "Date of diagnosis is greater than a regimen start date",
      DIAGNOSIS_OVER_SCT: "Date of diagnosis is greater than an SCT date",
      DIAGNOSIS_OVER_RESPONSE:
        "Date of diagnosis is greater than a response date",
      REGIMEN_OVERLAPS: "This regimen overlaps with another line of treatment",
    });

    $controller("PatientValidator", {
      $scope: $scope,
      $rootScope: $rootScope,
      toMomentFilter: toMomentFilter,
      $injector: mockInjector,
    });
  });

  describe("hoist onto rootscope", function () {
    it("Should hoise the PatientValidator onto $rootScope", function () {
      expect(!!$rootScope.patientValidator).toBe(true);
    });

    it("Should setup patient", function () {
      expect($rootScope.patientValidator.patient).toEqual(patient);
    });
  });

  describe("diagnosis_date", function () {
    var episode;
    var val;

    beforeEach(function () {
      episode = {
        regimen: [],
        sct: [],
        response: [],
      };
      $rootScope.patientValidator.patient.episodes = [episode];
    });

    it("should be fail if regimen date is below the diagnoisis date", function () {
      episode.regimen = [{ start_date: moment("2020-01-01") }];
      val = moment("2020-02-01");
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      var expected = "Date of diagnosis is greater than a regimen start date";
      expect($rootScope.patientValidator.errors.diagnosis_date).toBe(expected);
    });

    it("should not fail if regimen date is above the diagnosis date", function () {
      episode.regimen = [{ start_date: moment("2020-02-01") }];
      val = moment("2020-01-01");
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      expect(!!$rootScope.patientValidator.warnings.diagnosis_date).toBe(false);
    });

    it("should be fail if response date is below the diagnoisis date", function () {
      episode.response = [{ response_date: moment("2020-01-01") }];
      val = moment("2020-02-01");
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      var expected = "Date of diagnosis is greater than a response date";
      expect($rootScope.patientValidator.errors.diagnosis_date).toBe(expected);
    });

    it("should be fail if SCT date is below the diagnoisis date", function () {
      episode.sct = [{ sct_date: moment("2020-01-01") }];
      val = moment("2020-02-01");
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      var expected = "Date of diagnosis is greater than an SCT date";
      expect($rootScope.patientValidator.errors.diagnosis_date).toBe(expected);
    });

    it("should not fail if nothing is above the diagnosis date", function () {
      val = moment("2020-02-01");
      $rootScope.patientValidator.diagnosis_date(val, _, episode);
      expect(!!$rootScope.patientValidator.warnings.diagnosis_date).toBe(false);
    });
  });
});
