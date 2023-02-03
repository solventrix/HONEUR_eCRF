import io
import datetime
import csv
import logging
from django.utils.translation import gettext as _
from opal.models import Patient
from entrytool import models as entry_models
from plugins.conditions.mm import models as mm_models
from plugins.data_load.base_loader import Loader as BaseLoader
from django.db import transaction
from plugins.data_load.load_data import LoadError
from plugins.conditions.mm import episode_categories
from entrytool.episode_categories import LineOfTreatmentEpisode


class CologneLoader(BaseLoader):
    def get_and_check_external_identifier(self, column):
        value = self.row[column]
        try:
            if not value:
                logging.error(f"No external identifier found for {value}")
                raise ValueError(_("No external identifier found for %s") % value)
            if value:
                patients = Patient.objects.filter(demographics__hospital_number=value)
                if patients.exists():
                    logging.error(f"Patient {value} already exists")
                    raise ValueError(_("Patient %s already exists") % value)
        except Exception as err:
            self.add_error(column, value, str(err))
            return ""

        return self.check_and_get_string(
            entry_models.Demographics, "hospital_number", column
        )

    def check_and_get_date(self, column):
        value = self.row[column].strip()
        some_dt = None
        if value == "" or value == "-":
            return None
        try:
            some_dt = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except Exception:
            logging.error(f"Unable to convert {value} into a date with the format dd.mm.yyyy")
            description = (
                _("Unable to convert %s into a date with the format dd.mm.yyyy") % value
            )
            self.add_error(column, value, description)
        return some_dt

    def check_diagnosis(self):
        value = self.row["tatsächliche diagnose überprüft"]
        try:
            if not value == "MM":
                if not value:
                    logging.error("Diagnosis is not defined")
                    raise ValueError(_("Diagnosis is not defined"))
                else:
                    logging.error(f"{value} is not a recognised diagnosis")
                    raise ValueError(_("%s is not a recognised diagnosis"))
        except ValueError as err:
            self.add_error("tatsächliche diagnose überprüft", value, str(err))

    def unknown_value(self, column, expected_values):
        expected_values = ", ".join(expected_values)
        try:
            logging.error(f"Unexpected value {self.row[column]}")
            raise ValueError(
                _("Unexpected value %(value)s, expected one of %(expected_values)s")
                % {"value": self.row[column], "expected_values": expected_values}
            )
        except ValueError as err:
            self.add_error(column, self.row[column], str(err))

    def check_and_get_float(self, column):
        value = self.row[column].strip()
        if value == "":
            return None
        if value == "-":
            return None
        if "," in value:
            value = value.replace(",", ".")
        result = None
        try:
            result = float(value)
        except Exception:
            logging.error(f"Unable to convert {value} to a number")
            self.add_error(column, value, _("Unable to convert %s to a number") % value)
        return result

    def create_treatment_line(
        self,
        patient,
        start_date_column,
        end_date_column,
        regimen_column,
        maintenance_column=None,
        end_treatment_reason_column=None,
    ): 
        start_date = self.check_and_get_date(start_date_column)
        if self.row[end_date_column].strip() in ("ongoing", "entfällt", "unbekannt"):
            end_date = None
        else:
            end_date = self.check_and_get_date(end_date_column)
        # category = self.check_and_get_string(
        #     mm_models.MMRegimen, "category", category_column
        # )
        regimen_val = None
        if regimen_column:
            regimen_val = self.check_and_get_string(
                mm_models.MMRegimen, "regimen", regimen_column
            )
        end_treatment_reason = None
        if end_treatment_reason_column:
            end_treatment_reason = self.row[end_treatment_reason_column]

        if any([start_date, end_date, regimen_val, end_treatment_reason]):
            lot_episode = patient.episode_set.create(
                category_name=LineOfTreatmentEpisode.display_name
            )
            

            if maintenance_column:
                maintenance_regimen = lot_episode.mmregimen_set.create()
                maintenance_regimen.start_date = start_date
                maintenance_regimen.end_date = end_date
                maintenance_regimen.regimen = self.check_and_get_string(
                                                mm_models.MMRegimen, "regimen", maintenance_column 
                                            ) 
                maintenance_regimen.category = "Maintenance"
                maintenance_regimen.set_consistency_token()
                maintenance_regimen.save()    

            if "SCT" in regimen_val:
                lot_episode.mmstemcelltransplanteligibility_set.update(
                    eligible_for_stem_cell_transplant=True
                )
                eligible = lot_episode.mmstemcelltransplanteligibility_set.get()
                eligible.eligible_for_stem_cell_transplant = True
                eligible.set_consistency_token()
                eligible.save()
                sct = lot_episode.sct_set.create()
                sct.sct_type = "Unknown"
                sct.set_consistency_token()
                sct.save()

                ## Add Melphalan exposure as conditioning
                melphalan_regimen = lot_episode.mmregimen_set.create()
                melphalan_regimen.start_date = start_date
                melphalan_regimen.end_date = end_date
                melphalan_regimen.regimen = "Melphalan" 
                melphalan_regimen.category = "Conditioning"
                melphalan_regimen.set_consistency_token()
                melphalan_regimen.save()    

                ## Add VCD induction
                vcd_regimen = lot_episode.mmregimen_set.create()
                vcd_regimen.start_date = start_date
                vcd_regimen.end_date = end_date
                vcd_regimen.regimen = "VCD" 
                vcd_regimen.category = "Induction"
                vcd_regimen.set_consistency_token()
                vcd_regimen.save()
            else: 
                regimen = lot_episode.mmregimen_set.create()
                regimen.start_date = start_date
                regimen.end_date = end_date
                regimen.regimen = regimen_val
                if end_treatment_reason:
                    regimen.end_treatment_reason = end_treatment_reason
                regimen.set_consistency_token()
                regimen.save()
    def load_rows(self, data):
        pos = data.tell()
        dialect = csv.Sniffer().sniff(data.readline())
        data.seek(pos)
        rows = list(csv.DictReader(data, dialect = dialect))
        for _row in rows:
            row = {k.strip().lower(): v for k, v in _row.items()}
            self.idx += 1
            self.row = row
            self.load_row(row)
        return self.errors

    def load_row(self, data):
        hospital_number = self.get_and_check_external_identifier("patienten-nr.")
        if not hospital_number:
            return
        date_of_birth = self.check_and_get_date("geburtsdatum")
        gender_string = data["geschlecht"]
        gender = None
        if gender_string == "w":
            gender = "Female"
        elif gender_string == "m":
            gender = "Male"
        patient = Patient.objects.create()
        patient.patientload_set.update(
            source=entry_models.PatientLoad.LOADED_FROM_FILE
        )
        episode = patient.episode_set.create(
            category_name=episode_categories.MM.display_name
        )

        # ==== Demographics ====
        demographics = patient.demographics_set.get()
        demographics.hospital_number = hospital_number
        demographics.date_of_birth = date_of_birth
        demographics.sex = gender
        demographics.set_consistency_token()
        demographics.save()

        # ==== Patient Status ====
        patient_status = patient.patientstatus_set.get()
        patient_status.physician = self.check_and_get_string(
            entry_models.PatientStatus, "physician", "arzt"
        )
        date_of_last_contact_or_date_of_death = self.check_and_get_date(
            "datum des letzten kontakts oder sterbedatum"
        )
        patient_status.date_of_last_contact = date_of_last_contact_or_date_of_death

        deceased_status = self.row["verstorben an oder mit mm"]
        if deceased_status:
            patient_status.deceased = True
            if deceased_status == "mit":
                patient_status.death_cause = "Complications of Disease"
            elif deceased_status == "an":
                patient_status.death_cause = "Disease"
            elif deceased_status == "unbekannt":
                patient_status.death_cause = "Other"
            else:
                # If we don't know what it, put it on the model
                # and it will be flagged as an error by the validation
                patient_status.death_cause = deceased_status
            patient_status.death_date = date_of_last_contact_or_date_of_death
        patient_status.set_consistency_token()
        patient_status.save()

        # ==== Diagnosis ====
        self.check_diagnosis()
        diag_date = self.check_and_get_date(
            "datum erstdiagnose multiples myelom (idr kmp)"
        )
        diagnosis = episode.mmdiagnosisdetails_set.get()
        diagnosis.diag_date = diag_date

        high_risk_cytogenic = self.row[
            "hochrisiko zytogen. (a) del17p, b) t(4;14), 3) t(14;16)"
        ].strip()
        if not high_risk_cytogenic == "nein":
            if "t(4;14)" in high_risk_cytogenic:
                diagnosis.t4_14 = "Yes"
            if "del17p" in high_risk_cytogenic:
                diagnosis.del_17p = "Yes"
            if "t(14;16)" in high_risk_cytogenic:
                diagnosis.t4_14_16 = "Yes"

            other = (
                high_risk_cytogenic.replace("t(4;14)", "")
                .replace("del17p", "")
                .replace("t(14;16)", "")
                .strip("-;")
                .strip()
            )

            if len(other):
                self.unknown_value(
                    "hochrisiko zytogen. (a) del17p, b) t(4;14), 3) t(14;16)",
                    expected_values=["del17p", "t(4;14)", "t(14;16)"],
                )
        r_iss_bei_ed = self.row["r-iss bei ed"]
        if r_iss_bei_ed == "-":
            r_iss_bei_ed = None
        diagnosis.r_iss_stage = r_iss_bei_ed

        iss_mm_ed = self.row["iss mm ed"]
        if iss_mm_ed == "-":
            iss_mm_ed = None
        diagnosis.iss_stage = iss_mm_ed
        diagnosis.set_consistency_token()
        diagnosis.save()

        # ==== Lab Tests ====
        ldh = self.check_and_get_float("ldh u/l (norm bis 250)")
        beta2m = self.check_and_get_float("ß2m mg/l (<3,5 oder >5,5mg/l)")
        albumin = self.check_and_get_float("albumin g/l (>35g/dl = normal)")
        if ldh is not None or beta2m is not None or albumin is not None:
            lab_test = mm_models.LabTest.objects.create(
                LDH=ldh, beta2m=beta2m, albumin=albumin, episode=episode
            )
            lab_test.date = diag_date
            lab_test.hospital = "MVZ Koln"
            lab_test.set_consistency_token()
            lab_test.save()

        # === Line Of Treatments ===

        # Frontline
        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 1.-linie",
            end_date_column="datum ende 1.-linie",
            regimen_column="art der 1st-line",
            maintenance_column="erhaltungs-therapie",
            end_treatment_reason_column="keine therapie 2. linie grund",
        )
        # self.create_line_of_treatment(
        #     patient,
        #     start_date_column="datum beginn 1.-linie",
        #     end_date_column="datum ende 1.-linie",
        #     category_column="art der 1st-line",
        #     regimen_column="erhaltungs-therapie",
        #     end_treatment_reason_column="keine therapie 2. linie grund",
        # )
        # 2nd line
        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 2. linie2",
            end_date_column="datum ende 2. linie",
            regimen_column="art 2. linie2",
            maintenance_column="erhaltungstherapie 2. linie",
            end_treatment_reason_column="keine therapie 3. line grund2",
        ) 
        # self.create_line_of_treatment(
        #     patient,
        #     start_date_column="datum beginn 2. linie2",
        #     end_date_column="datum ende 2. linie",
        #     category_column="art 2. linie2",
        #     regimen_column="erhaltungstherapie 2. linie",
        #     end_treatment_reason_column="keine therapie 3. line grund2",
        # )

        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 3. linie2",
            end_date_column="datum beginn 3. linie2",
            regimen_column="art 3. linie",
            end_treatment_reason_column="keine therapie 4. line grund2",
        )
        

        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 4. linie",
            end_date_column="datum ende 4. linie",
            regimen_column="art der 4.linie",
            end_treatment_reason_column="keine 5. linie  grund",
        )

        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 5. linie",
            end_date_column="datum ende 5. linie",
            regimen_column="art der 5. linie",
            end_treatment_reason_column="warum keine 6. linie",
        )

        self.create_treatment_line(
            patient,
            start_date_column="datum beginn 6. linie",
            end_date_column="datum ende 6. linie",
            regimen_column="art der 6. linie",
        )


def _load_data(csv_file):
    if not csv_file.name.endswith(".csv"):
        return {"top_level_errors": [_("Please upload a csv file")], "row_errors": []}
    loader = CologneLoader(csv_file.name)
    file = csv_file.read().decode("utf-8")
    errors = loader.load_rows(io.StringIO(file))
    return {"top_level_errors": [], "row_errors": errors}


def load_data(csv_file):
    logging.info(f"Load CSV file {csv_file}")
    errors = {}
    try:
        with transaction.atomic():
            errors = _load_data(csv_file)
            if errors["top_level_errors"] or errors["row_errors"]:
                log_errors(errors)
                raise LoadError("rolling back transaction")
    except LoadError:
        pass
    return errors


def log_errors(errors):
    if not errors:
        logging.debug("No errors to log")
    else:
        if errors["top_level_errors"]:
            logging.error("top_level_errors: ")
            for error in errors["top_level_errors"]:
                logging.error(error)
        if errors["row_errors"]:
            logging.error("row_errors: ")
            for error in errors["row_errors"]:
                logging.error(error)

