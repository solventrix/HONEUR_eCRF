from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from django.db import models as fields
from opal.core.fields import ForeignKeyOrFreeText
from opal.core import lookuplists
from opal import models
from entrytool.models import Hospital


class MMRegimenList(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Regimen List")
        verbose_name_plural = _("MM Regimen List")


class MMStopReason(lookuplists.LookupList):
    class Meta:
        verbose_name = _("MM Stop Reason List")
        verbose_name_plural = _("MM Stop Reason List")


class MMPastMedicalHistory(models.PatientSubrecord):
    _is_singleton = True

    class Meta:
        verbose_name = _("Past Medical History")
        verbose_name_plural = _("Past Medical Histories")

    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    previous_neoplasm = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Previous Neoplasm")
    )
    previous_neoplasm_date_of_diagnosis = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    previous_neoplasm_details = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )

    previous_neoplasm_2 = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Prevous Neoplasm 2")
    )
    previous_neoplasm_date_of_diagnosis_2 = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    previous_neoplasm_details_2 = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )

    chronic_renal_insufficiency = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Chronic Renal Insufficiency")
    )
    chronic_renal_insufficiency_diagnosis_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Diagnosis Date")
    )

    # TODO Can we check this should not be a select field
    monoclonal_pathology = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Monoclonal Pathology")
    )
    symtomatic_multiple_myeloma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Symtomatic Multiple Myeloma")
    )

    asymtomatic_multiple_myeloma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Asymtomatic Multiple Myeloma")
    )

    monoclonal_pathology_of_uncertain_meaning = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Monoclonal Pathology Of Uncertain Meaning")
    )
    # TODO I am not sure this is correct
    monoclonal_pathology_of_uncertain_meaning_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Diagnosis Date")
    )

    external_pasmocytoma = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("External Pasmocytoma")
    )
    comments = fields.TextField(blank=True, default="", verbose_name=_("Comments"))


class MMDiagnosisDetails(models.EpisodeSubrecord):
    _is_singleton = True  # One entry per patient that is updated

    class Meta:
        verbose_name = _("Diagnosis Details")
        verbose_name_plural = _("Diagnosis Details")

    CHOICES = (("Yes", _("Yes")), ("No", _("No")),)

    ISS_DIAGNOSTIC_STATUS = (
        ("One", _("One")),
        ("Two", _("Two")),
        ("Three", _("Three")),
    )

    R_ISS_STAGES = (
        ("Stage I", _("Stage I")),
        ("Stage II", _("Stage II")),
        ("Stage III", _("Stage III")),
        ("Unknown", _("Unknown")),
    )

    # TODO seperate these out into the IgG, IGA, Light chain, no light chain etc
    # and Kappa and Llambda

    SUBCLASSIFICATION_CHOICES = (
            ("MM IgG Kappa", _("MM IgG Kappa"),),
            ("MM IgA Kappa", _("MM IgA Kappa"),),
            ("MM IgD Kapper", _("MM IgD Kapper"),),
            ("MM IgE Kapper", _("MM IgE Kapper"),),
            ("MM Light Chain Kappa", _("MM Light Chain Kappa"),),
            # No light chain


            ("MM IgG Lambda", _("MM IgG Lambda"),),
            ("MM IgA Lambda", _("MM IgA Lambda"),),
            ("MM IgD Lambda", _("MM IgD Lambda"),),
            ("MM IgE Lambda", _("MM IgE Lambda"),),
            ("MM Light Chain Lambda", _("MM Light Chain Lambda"),),

            ("Other", _("Other"),),
    )

    INFECTION_TYPE_CHOICES = (
        ("Clinically Documented Infection", _("Clinically Documented Infection")),
        ("Undocumented Infection", _("Undocumented Infection")),
        (
            "Microbiologically Documented Without Bacteremia",
            _("Microbiologically Documented Without Bacteremia")
        ),
        (
            "Microbiologically Documented With Bacteremia",
            _("Microbiologically Documented With Bacteremia")
        ),
        (
            "Other Microbiologic Documented Infection",
            _("Other Microbiologic Documented Infection"),
        )
    )

    DIAGNOSIS_OPTIONS = (
        ("Solitary Bone Plasmacytoma", _("Solitary Bone Plasmacytoma")),
        ("Symptomatic Multiple Myeloma", _("Symptomatic Multiple Myeloma")),
        ("Plasmatic Celiac Leukemia", _("Plasmatic Celiac Leukemia")),
        ("Primary Amylodosis", _("Primary Amylodosis")),
        ("Asymptomatic MM", _("Asymptomatic MM")),
    )

    date_of_diagnosis = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of Diagnosis")
    )
    date_of_first_centre_visit = fields.DateField(
        blank=True, null=True, verbose_name=_("Date Of First Centre Visit")
    )

    referred = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Referred")
    )
    previous_hospital = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Previous Hospital")
    )

    infection_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=INFECTION_TYPE_CHOICES,
        verbose_name=_("")
    )
    diagnosis = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=DIAGNOSIS_OPTIONS,
        verbose_name=_("Diagnosis")
    )
    subclassification = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SUBCLASSIFICATION_CHOICES,
        verbose_name=_("SUBCLASSIFICATION")
    )

    iss_diagnostic_status = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=ISS_DIAGNOSTIC_STATUS,
        verbose_name=_("ISS Diagnostic Status")
    )

    riss_stage = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=R_ISS_STAGES,
        verbose_name=_("R-ISS Stage")
    )

    # GAH Score 0 to 94
    gah_score = fields.IntegerField(
        blank=True, null=True, verbose_name=_("GAH Score")
    )
    # IMWG Scale 1 to 8
    imwg_scale = fields.IntegerField(
        blank=True, null=True, verbose_name=_("IMWG Scale")
    )
    # ICC scale 0 to 31
    cc_scale = fields.IntegerField(blank=True, null=True, verbose_name=_("ICC Scale"))

    ircp_diag_date = fields.DateField(
        blank=True, null=True, verbose_name=_("IRCP Diagnosis Date")
    )

    # these fields are what the spread sheet call generics, putting them
    # here for want of a better place.
    height = fields.IntegerField(blank=True, null=True, verbose_name=_("Height"))

    # kg
    weight = fields.FloatField(blank=True, null=True, max_length=256, verbose_name=_("Weight"))
    pres_clinical_renal_failure = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Pres Clinical Renal Failure")
    )
    pres_clinical_hypercalcemia = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Pres Clinical Hypercalcemia")
    )
    pres_clinical_fever = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Pres Clinical Fever")
    )
    pres_clinical_anemia = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Pres Clinical Anemia")
    )

    bone_pain_pres_clinic = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Pres Clinical Bone Pain")
    )

    # the name of the micro organism
    pres_clinical_microorganism = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Pres Clinical Microorganism")
    )

    pres_clinical_description = fields.TextField(
        blank=True, default="", verbose_name=_("Pres Clinical Description")
    )

    # TODO, not sure what this is, can we remove it?
    microorg_pc_focus = fields.CharField(
        blank=True,
        null=True,
        max_length=256
    )

    extramedullary_plasmacytomas = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Extramedullary plasmacytomas")
    )

    # 0-5 scale
    ecog = fields.IntegerField(blank=True, null=True, verbose_name=_("ECOG"))
    dialysis = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Dialysis")
    )

    epidemiologic_registry = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Epidemiologic registry")
    )


class Cytogenetics(models.EpisodeSubrecord):

    class Meta:
        verbose_name = _("Cytogenetics")
        verbose_name_plural = _("Cytogenetics")

    CHOICES = CHOICES = (("Yes", _("Yes")), ("No", _("No")), ("Unknown", _("Unknown")),)

    t4_14_not_effected = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("t(4;14) Not Effected")
    )
    t4_14_haploid_karyotype = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("t(4;14) Haploid Karyotype")
    )
    t4_14 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(4;14)")
    )
    t4_14_16 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(14;16)")
    )
    t11_14 = fields.CharField(
        max_length=10,
        blank=True,
        null=True,
        choices=CHOICES,
        verbose_name=_("t(11;14)")
    )
    # TODO check thisis the same as del 14, as we require this for data to be a superser
    # of the default MM
    del1p = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("del 1p")
    )

    del_17p = fields.CharField(
        max_length=10, choices=CHOICES, verbose_name=_("del(17)p")
    )

    # TODO I can't find a reference to this so I'm not sure the display name
    # is correct
    gan1q = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("gan 1q")
    )

    chromosome_alterations = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Chromosome Alterations")
    )

    normal_study = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Normal Study")
    )
    description = fields.TextField(blank=True, default="", verbose_name=_("Description"))
    other_study = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CHOICES,
        verbose_name=_("Other study")
    )


class PatientOutcome(models.PatientSubrecord):

    class Meta:
        verbose_name = _('Patient Outcome')
        verbose_name_plural = _('Patient Outcomes')

    OUTCOME_CHOICES = (
        ("Complete Response Molecular", _("Complete Response Molecular"),),
        ("Complete Response Immunophenotypic", _("Complete Response Immunophenotypic"),),
        ("Complete Response Strict", _("Complete Response Strict"),),
        ("Very Good Partial Response", _("Very Good Partial Response"),),
        ("Partial Response", _("Partial Response"),),
        ("Stable Disease", _("Stable Disease"),),
        ("Progression", _("Progression"),),
        ("Unknown", _("Unknown"),),
        ("Death", _("Death"),),
    )

    CAUSE_OF_DEATH = (
        ("Multiple Myeloma", _("Multiple Myeloma"),),
        ("Infection", _("Infection"),),
        ("Thrombosis", _("Thrombosis"),),
        ("Not Disease Related", _("Not Disease Related"),),
        ("Not Available", _("not available"),),
        ("Other", _("Other")),
    )
    STATUS_CHOICES = (
        ("Dead", _("Dead"),),
        ("Lost", _("Lost"),),
        ("Alive", _("Alive"),),
    )

    outcome_at_the_last_visit = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=OUTCOME_CHOICES,
        verbose_name=_("Outcome At The Last Visit")
    )
    status = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=STATUS_CHOICES,
        verbose_name=_("Status")
    )
    status_date = fields.DateField(blank=True, null=True, verbose_name=_("Date"))
    comments = fields.TextField(
        blank=True,
        null=True,
        verbose_name=_("Comments")
    )
    cause_of_death = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CAUSE_OF_DEATH,
        verbose_name=_("Cause Of Death")
    )
    cause_of_death_other = fields.TextField(
        blank=True, default="", verbose_name=_("Details")
    )


class LabTests(models.EpisodeSubrecord):
    GLOMERULAR_FILTRATION_FORMULA = (
        ("MDRD", _("MDRD"),),
        ("CKD-EPI", _("CKD-EPI"),),
        ("Other", _("Other"),),
    )

    # mg/L min 3 max 30
    pcr = fields.IntegerField(blank=True, null=True, verbose_name=_("PCR"))

    # x109/L
    celulas_plasmaticas_circulantes = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Celulas Plasmaticas Circulantes")
    )

    # Troponine I, ng/L, min 0 max 350
    troponina = fields.IntegerField(blank=True, null=True, verbose_name=_("Troponina"))
    total_proteins = fields.IntegerField(blank=True, null=True, verbose_name=_("Total Proteins"))

    platelets = fields.IntegerField(blank=True, null=True, verbose_name=_("Platelets"))

    # mg/L min 1.5 max 20
    beta_2_microglobulin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Beta 2 Microglobulin")
    )
    alkaline_phosphatase = fields.IntegerField(
        blank=True,
        null=True,
        verbose_name=_("Alkaline Phosphatase")
    )
    # g/dL min 1 max 5.5
    albumin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Albumin")
    )

    # mg/dL, min 0.5, max 20
    creatinine = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Creatinine")
    )

    # mg/dL, min 6.5, max 25
    calcium = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Calcium")
    )

    hemoglobin = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Hemoglobin")
    )

    proteinuria = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Proteinuria")
    )
    proteinuria_g24 = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Proteinuria gr/24")
    )

    # x109/L min 1 max 100
    leucocytes = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Leucocytes")
    )

    nt_pro_bnp = fields.IntegerField(
        blank=True, null=True, verbose_name=_("NT-proBNP")
    )

    ldh = fields.IntegerField(
        blank=True, null=True, verbose_name=_("LDH")
    )
    ldh_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("LDH Type")
    )

    glomerular_filtration_formula_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Glomerular Filtration Formula Date")
    )
    glomerular_filtration_formula = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=GLOMERULAR_FILTRATION_FORMULA,
        verbose_name=_("Glomerular Filtration Formula")
    )

    # mL/min, min 5 max 102
    glomerular_filtration = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Glomerular Filtration")
    )

    filter_formula_description = fields.TextField(
        blank=True, default="", verbose_name=_("Filter Formula Description")
    )


class Imaging(models.EpisodeSubrecord):

    class Meta:
        verbose_name = 'Imaging'
        verbose_name_plural = 'Imaging'

    BONE_SERIES_TEST_IMAGE_OPTIONS = (
        ("Zero", _("Zero")),
        ("One", _("One")),
        ("Two", _("Two")),
        ("Three", _("Three")),
    )

    YES_NO = (
        ("Yes", _("Yes"),),
        ("No", _("No"),)
    )

    SCAN_OPTIONS = (
        ("Negative", _("Negative")),
        ("Positive", _("Positive")),
        ("Not Done", _("Not Done")),
    )

    bone_series_test_image = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=BONE_SERIES_TEST_IMAGE_OPTIONS,
        verbose_name=_("Bone Series Test Image")
    )
    # this has never been used
    bone_series_description = fields.TextField(
        blank=True, default="", verbose_name=_("Bone Series Description")
    )
    ct_scan = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("CT Scan")
    )
    ct_scan_description = fields.TextField(
        blank=True, default="", verbose_name=_("CT Scan Description")
    )

    resonance = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("Resonance")
    )
    resonance_description = fields.TextField(
        blank=True, default="", verbose_name=_("Resonance description")
    )

    pet_scan = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=SCAN_OPTIONS,
        verbose_name=_("PET scan")
    )
    pet_scan_description = fields.TextField(
        blank=True, default="", verbose_name=_("PET scan description")
    )

    other_imaging_test = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=YES_NO,
        verbose_name=_("Other Imaging Test")
    )
    other_imaging_test_description = fields.TextField(
        blank=True, default="", verbose_name=_("Other Imaging Test Description")
    )


class ConditionAtInduction(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _('Condition at induction')
        verbose_name_plural = _('Conditions at induction')

    INFECTION_TYPES = (
        ("Undocumented Preinfection", _("Undocumented Preinfection"),),
        ("Microbiologically Documented Without Bacteremia", _("Microbiologically Documented Without Bacteremia"),),
        ("Microbiologically Documented With Bacteremia", _("Microbiologically Documented With Bacteremia"),),
        ("Clinically Documented", _("Clinically Documente"),),
    )

    CONDITION_TYPES = (
        ("Renal Failure", _("Renal Failure"),),
        ("Neuropathy", _("Neuropathy"),),
        ("Hemorrhage", _("Hemorrhage"),),
        ("Fever", _("Fever"),),
        ("Infection", _("Infection"),),
        ("Other", _("Other"),),
    )
    condition = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=CONDITION_TYPES,
        verbose_name=_("Condition")
    )

    # if condition == infection
    infection_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=INFECTION_TYPES,
        verbose_name=_("Infection Type")
    )
    type_of_microorganism_infection = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Type Of Microorganism Infection")
    )
    infection_source = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Infection Source")
    )

    # if condition == other
    other_condition_name = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Condition Name")
    )


class MMRegimen(models.EpisodeSubrecord):
    _sort = "start_date"
    order_by = "-start_date"

    REGIMEN_TYPES = (
        ("Induction", _("Induction")),
        ("Maintenance", _("Maintenance")),
        ("Conditioning", _("Conditioning")),
        ("Watch and wait", _("Watch and wait")),
    )

    EMR2_TECHNIQUE_OPTIONS = (
        ("NGS", _("NGS"),),
        ("FC (Flow Cytometry)", _("FC (Flow Cytometry)"),),
        ("Both", _("Borth")),
    )

    YES_NO = (
        ("Yes", _("Yes"),),
        ("No", _("No"),)
    )

    hospital = models.ForeignKeyOrFreeText(Hospital, verbose_name=_("Hospital"))
    nbCycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date = fields.DateField(
        verbose_name=_("Start Date"),
    )
    end_date = fields.DateField(verbose_name=_("End Date"), blank=True, null=True)
    response_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Response Date")
    )
    regimen = ForeignKeyOrFreeText(MMRegimenList, verbose_name=_("Regimen"))
    regimen_description = fields.TextField(
        blank=True, default="", verbose_name=_("Regimen Description")
    )
    category = fields.CharField(
        max_length=40, choices=REGIMEN_TYPES, verbose_name=_("Regimen Type")
    )
    stop_reason = ForeignKeyOrFreeText(
        MMStopReason, verbose_name=_("Reason for Regimen Stop")
    )
    stop_reason_description = fields.TextField(
        blank=True, default="", verbose_name=_("Stop Reason Description")
    )
    comments = fields.TextField(blank=True, default="", verbose_name=_("Comments"))

    # Technique used to determine negative MRD
    emr_technique = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=EMR2_TECHNIQUE_OPTIONS,
        verbose_name=_("EMR2 Technique")
    )

    negative_mrd = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=YES_NO,
        verbose_name=_("Negative MRD")
    )
    negative_mrd_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Negative MRD Date")
    )

    class Meta:
        verbose_name = _("Regimen")
        verbose_name_plural = _("Regimens")


class BoneDisease(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Bone Disease Treatment")
        verbose_name_plural = _("Bone Disease Treatments")

    TREATMENT_TYPES = (
        ("Denosumab", _("Denosumab"),),
        ("Bisphosphonates Induction", _("Bisphosphonates Induction"),),
        ("Vertebroplasty Induction", _("Vertebroplasty Induction"),),
        ("Others Induction", _("Others Induction"),),
        ("Not Available", _("Not Available"),),
    )
    treatment_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=TREATMENT_TYPES,
        verbose_name=_("Treatment Type")
    )

    # only for treatment type Bisphosphonates
    bisphosphonate_treatment = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Bisphosphonate Treatment")
    )
    nb_cycles = fields.IntegerField(
        verbose_name=_("Number of Cycles"),
        null=True,
        blank=True,
    )
    start_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    end_date = fields.DateField(
        blank=True, null=True, verbose_name=_("End Date")
    )
    vertebroplasty_kyphoplasty_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Vertebroplasty Kyphoplasty Date")
    )
    vertebroplasty_kyphoplasty_description = fields.TextField(
        blank=True, default="", verbose_name=_("Vertebroplasty Kyphoplasty Description")
    )


class MMResponse(models.EpisodeSubrecord):
    _sort = "response_date"
    order_by = "-response_date"

    class Meta:
        verbose_name = _("Response")
        verbose_name_plural = _("Responses")

    RESPONSES = (
        ("Minimal response", _("Minimal response")),
        ("Partial response", _("Partial response")),
        ("Very good partial response", _("Very good partial response")),
        ("Complete response", _("Complete response")),
        ("Stringent complete response", _("Stringent complete response")),
        ("Near complete response", _("Near complete response")),
        ("Immunophenotypic complete response", _("Immunophenotypic complete response")),
        ("Stable disease", _("Stable disease")),
        ("Progressive disease", _("Progressive disease")),
        ("Response unknown/NA", _("Response unknown/NA")),
    )
    response_date = fields.DateField(blank=True, null=True, verbose_name=_("Response Date"))
    response = fields.CharField(
        max_length=50, choices=RESPONSES, verbose_name=_("Response")
    )


# lab tests
class MProteinMesurements(models.EpisodeSubrecord):
    HEAVY_CHAIN_OPTIONS = (
        ("IgG", _("IgG"),),
        ("IgD", _("IgD"),),
        ("IgA", _("IgA"),),
        ("IgM", _("IgM"),),
        ("IgE", _("IgE"),),
        ("No Heavy Chain", _("No Heavy Chain"),),
        ("Other", _("Other"),),
    )
    LIGHT_CHAIN_OPTIONS = (
        ("IgA", _("IgA"),),
        ("IgD", _("IgD"),),
        ("IgE", _("IgE"),),
        ("IgG", _("IgG"),),
        ("IgM", _("IgM"),),
    )

    serum_amount = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Monoclonal serum amount")
    )
    heavy_chain_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=HEAVY_CHAIN_OPTIONS,
        verbose_name=_("Heavy Chain Type")
    )
    # I don't think we need this but...
    heavy_chain_type_other = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Heavy Chain Type Other")
    )
    light_chain_type = fields.CharField(
        blank=True,
        null=True,
        max_length=256,
        choices=LIGHT_CHAIN_OPTIONS,
        verbose_name=_("Light Chain Type")
    )

    lambda_light_chain_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Lambda Light Chain Count")
    )
    kappa_light_chain_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Kappa Light Chain Count")
    )
    kappa_lambda_ratio = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Kappa Lambda Ratio")
    )

    urinary_monoclonal_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Urinary Monoclonal Count gr/24")
    )

    plasma_cells_in_bone_marrow = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Plasma Cells In Bone Marrow %")
    )
    freelite_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Freelite Count")
    )
    heavylite_count = fields.FloatField(
        blank=True,
        null=True,
        max_length=256,
        verbose_name=_("Heavylite Count")
    )


class Radiotherapy(models.EpisodeSubrecord):
    class Meta:
        verbose_name = _("Radiotherapy")
        verbose_name_plural = _("Radiotherapies")

    start_date = fields.DateField(
        blank=True, null=True, verbose_name=_("Start Date")
    )
    end_date = fields.DateField(
        blank=True, null=True, verbose_name=_("End Date")
    )


class MMStemCellTransplantEligibility(models.EpisodeSubrecord):
    _is_singleton = True
    eligible_for_stem_cell_transplant = fields.BooleanField(default=False)

    class Meta:
        verbose_name = _("Stem Cell Transplant Eligibility")
        verbose_name_plural = _("Stem Cell Transplant Eligibilities")


def delete_stem_cells(sender, instance, **kwargs):
    instance.episode.sct_set.all().delete()


post_save.connect(
    delete_stem_cells, sender=MMStemCellTransplantEligibility
)
