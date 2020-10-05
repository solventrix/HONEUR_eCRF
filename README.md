This is Honeur eCRF - an application for recording patient treatment data.

This project is built using the [Opal](https://github.com/openhealthcare/opal) framework.

## Installation And Setup

To get started, run the following commands:

```
git clone git@github.com:solventrix/HONEUR_eCRF.git
cd HONEUR_eCRF
mkvirtualenv -a $PWD honeur-ecrf
pip install -r requirements.txt
python manage.py migrate
python manage.py load_lookup_lists
python manage.py createopalsuperuser
python manage.py runserver
```

## Loading data

To load in data we expect 3 csvs. Patients are connected by the hospital
number column (headed `Hospital_patient_ID`).

```
python manage.py load_demographics {{ path_to_demographics_csv }}
python manage.py load_lot {{ path_to_treatments.csv }}
python manage.py load_followup {{ path_to_followup_csv }}
```

## Application Administration

### Adding a user

To add a user you must have a user account with relevant privileges.

1. Log in to the application
2. Click the Admin button
3. In the AUTHENTICATION AND AUTHORIZATION heading click the Add button next on the Users row.
4. Complete the user details and an initial password for the user
5. Click the Save button

## Data Validation

Most simple data validation is done via expressing the rules on either the
models themselves, or in the form templates.

Some of this validation - for instance fields being required is implemented within Opal,
while some is implemented with custom form widgets as part of the entrytool application.

### Relative Date Validation

We sometimes wish to validate that a date is before, or after another date.

For instance that an end date is after a start date.

For simple cases, this can be done using the `{% custom_datepicker %}` templatetag.

Date validation requires two arguments:

* `date_after` a javascript reference to the other date value that we would like to validate against
* `date_after_message` a string that should be displayed when the date entered is invalid

An optional third argument allows for an offset to be specified

* `date_after_diff` which is a number that will be used as an offset when validating

The same options are also available for date_before.

For example:

```
{% custom_datepicker field="AdverseEvent.ae_date"
   date_after="the_episode.regimen[0].start_date"
   date_after_message="Adverse event must be on or after the regimen start date"
   date_after_diff="0"
   date_before="the_episode.regimen[0].end_date"
   date_before_message="Adverse event must be before 30 days after the regimen end date"
   date_before_diff="31"
   required=True %}
```
