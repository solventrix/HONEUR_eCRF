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

### Re-setting your database in development

To flush your database and 'start again' in deveopment - for instance to test load scripts for a new deployment, run the following commands:

```
python manage.py flush
python manage.py load_lookup_lists
python manage.py createopalsuperuser
```

## Application Administration

### Adding a user

To add a user you must have a user account with relevant privileges.

1. Log in to the application
2. Click the Admin button
3. In the AUTHENTICATION AND AUTHORIZATION heading click the Add button next on the Users row.
4. Complete the user details and an initial password for the user
5. Click the Save button

### Deployment Notes

Deploying Opal applications should be broadly similar to deploying any Django application. We include here some specific notes to consider when designing that process.

It is expected that you will generate a new Django secret key on deployment as the one in the current `settings.py` file is linked to the Opal version rather than generated randomly at project start time.

In addition to standard Django deployment management commands (e.g. `collectstatic`) we would recommend you run the following command at deploy time:

`python manage.py load_lookup_lists`

This ensures reference data in the database contains all the values required.

Production deployments would not be expected to run sqlite, which is only suited to development environments. Example configuration for PostgreSQL can be found in the [Django documentation](https://docs.djangoproject.com/en/2.2/ref/settings/#std:setting-HOST). The section on [deploying Django](https://docs.djangoproject.com/en/3.1/howto/deployment/) will also be helpful.

## Customising the look and feel of the application

The visual style of the application is defined in the template files as HTML structure and Bootstrap CSS classes and in the application specific css. We use [Sass](https://sass-lang.com/) compiled to css in order to take advantage of features such as variables for colors.

Changes to CSS should be made in the file `entrytool/static/css/entrytool.scss` and compiled to css using the sass commandline tool. While changing the scss file, run:

`sass -w entrytool/static/css/entrytool.scss`

This will watch for changes to the scss file and compile them to css whenever the scss file is
saved. Once you are happy with your changes, commit the updated css, scss and css.map files together.

### Making edit buttons permanently visible

To make editing controls permanently visible, uncomment this line in the `.scss` file and recompile:

```

.entry-tool{
    .panel-heading i.edit,
    .list-group-item i.edit,
    .list-group-item i.delete{
        // display:block
    }
```

## Customising the fields in the application

Customising fields in the application is intended to be a reasonably simple process, which will involve some combination of altering templates for display and forms, database structure, and potentially validation. Validation is dealt with in it’s own section within this document and will be omitted here.

Note: In this document sequences of $ALLCAPS beginning with a $ sign refer to ‘variables’ - that is to say you should substitute in values relevant to the context in question. This will almost never be in CAPITALS. There will mostly be other examples of such code within the application you can refer to as a reference.

### Customising particular deployments

In this section we will consider a number of potential likely use cases that have been outlined for customising individual deployments of the application.

#### Hiding fields

First we will need to examine the model declaration for the field in question - this will be a property of a class in the file `entrytool/models.py`. It is recommended to not alter the database and remove fields from the core application if they are being hidden in a particular deployment in order to avoid unnecessary database migration history conflicts. If the field declared in the `models.py` file has the argument `null=True` then we need to take no action here. If this argument is missing or set to `null=False` we will have to change this by:

Set the argument `null=True` in the model field declaration
Generate a migration by running `python manage.py makemigrations`
Run that migration `python manage.py migrate`

We will need to remove the field from the form template. This will be located in a file with a name based on the name of the model at `entrytool/templates/forms/$MODELNAME_form.html`. We should be able to find a templatetag declaring and configuring the form widget in use for that field by searching in the file for a string like `field=“$MODELNAME.$FIELDNAME”`. We can then delete that line.

We should also ensure that there are no display artefacts related to the field. The display template for a model is found in a file based on the name of the model at `entrytool/templates/records/$MODELNAME.html`. That file will render the data from instances of that model using the syntax `[[ item.$FIELDNAME ]] ` you should search for this declaration and remove it to avoid unnecessary clutter in the display template.

#### Adding a field to a model

First we will need to find the model declaration in `entrytool/modelspy` and add a new field declaration to the model. This process is extensively documented by Django itself and many other examples can be seen within the `models.py` file itself. Once the field has been declared in the models.py file we should update the database to match:

1. `python manage.py makemigrations`
2. `python manage.py migrate`

We will now need to add a widget for our field to the form for this model. This will be located in a file with a name based on the name of the model at `entrytool/templates/forms/$MODELNAME_form.html`. We then add a template tag matching the widget we would like - for instance to add a text box `{% input field=“$MODELNAME.$FIELDNAME” %}. You can see many examples in the form templates within this application, and additional documentation is available on the Opal website.

We will now be required to update the display template for the model to include this data in the patient detail display. The display template for a model is found in a file based on the name of the model at `entrytool/templates/records/$MODELNAME.html`. Display data is rendered via Javascript in the browser, so uses the square bracket syntax. Display templates will have a variable named `item` which contains the data for the instance of the model we are rendering. You can display a field with for instance:

```
<h1>[[ item.$FIELDNAME ]]</h1>
```

#### Adding a new set of data to lines of treatment

Adding an entirely new set of data will require creating a new model in `entrytool.models.py`. This is a python class the inherits from `opal.models.EpisodeSubrecord` that generates a new table in the database. This process is documented extensively by Django, Opal specific alterations (mostly additional properties that are available) are documented in the Opal documentation, and the models `SCT`, `Regimen`, `Response` and `AdverseEvent` provide examples within this application.

Once the model is created the database needs to be updated:

1. `python manage.py makemigrations`
2. `python manage.py migrate`

We can then create form and display templates for this model by running `python manage.py scaffold entrytool` this will create the templates in `entrytool/templates/records/$MODELNAME.html` and `entrytool/templates/forms/$MODELNAME_form.html`. These can be edited to adjust widgets in use, or refine the layout of individual records. The other templates in the folders `entrytool/templates/records/` and `entrytool/templates/forms` should serve as an example of how these can be adjusted.

The new model will then need to be added to the line of treatment template at `entrytool/templates/detail/treatmentline.html` with a new record panel declaration `{% record_panel models.$MODELNAME %}`. The location of this panel relative to the others can be adjusted by editing this template’s layout as defined by the Bootstrap css classes e.g. `row` and `col-md$X`. The bootstrap website has extensive documentation for creating layouts using these classes, and this application contains many examples.

## Data Validation

Most simple data validation is done via expressing the rules on either the
models themselves, or in the form templates.

Some of this validation - for instance fields being required is implemented within Opal,
while some is implemented with custom form widgets as part of the entrytool application.

### Num ber validation
We sometimes wish to validate that a number is more or less
than a number. this can be done using the `{% number %}` templatetag.

Min validation is done with the `min_value` argument, Max_validation is done with the `max_value` argument.

We can also warn a user if a number is outside the usual bounds. This will not error but display a warning message. This is done with the `warn_min` and `warn_max` arguments.

for example

```
{% number min_value="0" warn_min="5", max_value="100" warn_max="95"}
```



### Relative Date Validation

We sometimes wish to validate that a date is before, or after another date.

For instance that an end date is after a start date.

For simple cases, this can be done using the `{% custom_datepicker %}` templatetag.

Date validation requires two arguments:

* `date_after` a javascript reference to the other date value that we would like to validate against
* `date_after_message` a string that should be displayed when the date entered is invalid. Wrap it in an an `_()` method call to make sure that it is translated.

An optional third argument allows for an offset to be specified

* `date_after_diff` which is a number that will be used as an offset when validating

The same options are also available for date_before.

For example:

```
{% custom_datepicker field="AdverseEvent.ae_date"
   date_after="the_episode.regimen[0].start_date"
   date_after_message=_("Adverse event must be on or after the regimen start date")
   date_after_diff="0"
   date_before="the_episode.regimen[0].end_date"
   date_before_message=_("Adverse event must be before 30 days after the regimen end date")
   date_before_diff="31"
   required=True %}
```

## Batch Imports

It is possible to import data into the system using a batch file load. This is currently implemented as a series of Django management commands that process and save CSV files. The standard implementation expects 3 files, covering demographics, lines of treatment, and follow up visits/lab measurements. Patients are connected by the hospital number column (headed `Hospital_patient_ID`).

These importers can be run using the following commands:

```
python manage.py load_demographics $PATH_TO_FILE
python manage.py load_lot $PATH_TO_FILE
python manage.py load_followup $PATH_TO_FILE
```

### Altering the importers

Simple alterations to the importers can be made by altering the field mappings at the top of each file. This is a variable named `field_map` which contains a python dictionary specifying the model field that each column name from the CSV that relates to.

#### Adding a new field to an importer

Should we wish to add an entire new field to an importer, we would first need to add that field to the application itself. This is covered in the section on customisation elsewhere in this document.

For this example we will assume that a new field `wcc` has been added to the `FollowUpVisit` model that records the white cell count for the patient at that time. The importer can also be adjusted to add that field. We would first alter our CSV files by adding a new column, headed `wcc` with those values.

Next we would add that field to the `field_map` variable in `entrytool/management/commands/load_followup.py` using `wcc=“wcc”` - a dictionary key and a string representing the header value.

Finally we add the new field to the Follow up creation - in this case a variable named `followup_fields` that contains a mapping of field names to values for individual rows in the CSV just before they are saved. We would add to this dictionary using a string representing the model field name (“wcc”) mapping to the value we would like to use. The row from the CSV is stored in the variable `follow_up_row` which is a python dictionary that can be accessed using the CSV headers as keys. We use our `field_map` variable to source these.

We may also like to do some data sanitisation and cast the CSV data to an appropriate type at this stage - a group of utility functions for this exist in the module `entrytool.load_utils`. In this instance we would be likely to use the `float_or_none` function. The line we would add to the `followup_fields` dictionary would be something like:

`”wcc”: float_or_none(follow_up_row[field_map[“wcc”]]),`

#### Adding a new reading to follow ups that already exist

Although we have not written a management command for this task explicitly, the import script for this would likely be short and simple to create. The basic version would require 10 lines of python, plus some boilerplate required by Django. Using our example of adding White Cell Count from above, should we wish to add this to existing follow up entries, we would generate a CSV containing the fields `external_identifier`, `date`, `wcc`.

Django management commands are python files in the directory `entrytool/management/commands` and contain a class inheriting from `BaseCommand`. The command runs the code in the `handle` method. A simple management command to print a CSV is available as an example in the file `entrytool/management/commands/print_csv.py`.

To add WCC readings to existing follow ups we would create a new management command using this as a template - a file named `entrytool/management/commands/load_wcc.py`. We must then alter our process_rows method to:

* Find the correct followup
* Save the new reading

This code might read as follows:

```python
from entrytool.models import FollowUp, Demographics
from entrytool.load_utils import cast_date, int_or_none

for row in rows:
    patient = Demographics.objects.get(
        external_identifier=row['external_identifier']).patient
    follow_up = FollowUp.objects.get(
        patient=patient, follow_up_date=cast_date(row['date'])
    )
    follow_up.wcc = int_or_none(row['wcc'])
    follow_up.save()
```

## Alternative Follow up page.

The follow up page at the moment works well for 8-10 follow up fields. There are currently 8, so this allows room. Should you wish to have a deployment with more than 8 fields. An alternative display might look like the below. This displays the fields vertically and the
date stamps of the last 8 results at the top. This loses the ability to see more than 8
results in the history, but gains the ability for any number of fields.

To replace this change the template file `entrytool/detail/followups.html` to the below text.


```
{% load i18n %}
<div class="follow-up-table" ng-show="episode.follow_up.length > 0">
<span ng-repeat="item in [episode.follow_up[]] | orderBy: '-follow_up_date' as follow_ups"></span>
  <div class="col-md-12">
    <div class="row header-row display-label">
      <div class="col-sm-3 header"></div>
      <div ng-show="$index < episode.follow_up.length" class="col-sm-1 header" ng-repeat="not_used in [].constructor(8) track by $index">
        <span ng-show="$index < follow_ups.follow_up.length">
          [[ follow_ups[$index].hospital | translate ]]
          <br />
          [[ follow_ups[$index].follow_up_date | displayDate ]]
          <br>
          <i style="font-size: 14px;" ng-click="episode.recordEditor.editItem('{{ models.FollowUp.get_api_name }}', follow_ups[$index])" class="fa fa-pencil edit pointer"></i>
        </span>
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "LDH" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].LDH ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "Beta2m" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].beta2m ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "Albumin" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].albumin ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "Creatinin" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].creatinin ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "MCV" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].MCV ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "Hb" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].Hb ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">&#922;/&#923; Ratio</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].kappa_lambda_ratio ]]
      </div>
    </div>
    <div class="row table-row" >
      <div class="col-sm-3 first-column text-right">{% trans "Bone Lesions" %}</div>
      <div class="col-sm-1 column" ng-repeat="not_used in [].constructor(8) track by $index">
        [[ follow_ups[$index].bone_lesions ]]
      </div>
    </div>
  </div>
</div>
```



## Customisation of search results

Search results are generated by passing the search string as a query to a list of predefined database fields. These can be adjusted by changing the setting `OPAL_SEARCH_FIELDS`. The syntax for this list of fields matches that of the (Django Queryset)[https://docs.djangoproject.com/en/3.1/ref/models/querysets/#queryset-api] API. The fields in this setting will be used as arguments to a filter query on the Patient model.


## Alternative authentication methods

It is possible to configure the application to use alternative authentication backends.

### LDAP authentication

A third party package (django-auth-ldap)[https://django-auth-ldap.readthedocs.io/en/1.6.1/authentication.html] provides LDAP integration. Example settings for these can be found in the file `entrytool/settings.py`. The first step would be to uncomment the `  ‘django_auth_ldap.backend.LDAPBackend',` backend from the `AUTHENTICATION_BACKENDS` setting. Then we must configure the application to know about the specific LDAP server we will use by adjusting the `AUTH_LDAP_*` settings

The settings file contains a commented out short logging reconfiguration that will increase the log level for just the LDAP authentication while doing initial configuration.

### Custom auth backends

It is also possible to write a custom authentication backend for Django that uses any arbitrary authentication method. This requires changing the AUTHENTICATION_BACKENDS setting and implementing a new subclass of `BaseBackend`. This process is (documented by Django)[https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#writing-an-authentication-backend].

## How to retrieve previous values of data

Previous values of data from within the application that has been changed via the UI are stored by (Django Reversion)[https://django-reversion.readthedocs.io/en/stable/]. This stores all incremental versions of Opal Subrecords as JSON data as well as deleted versions. The integration within the Admin will allow users to navigate to previous versions and examine change history as well as roll back unwanted edits / deletions.

Previous versions can be accessed either by the (Reversion Python API)[https://django-reversion.readthedocs.io/en/stable/api.html#loading-revisions] or by extracting the JSON representation from the reversion_version table. Once deserialised these will contain references to the entry tool unique patient ID of the form "patient": 2416, or to Episode IDs.

Selecting rows related to a specific patient and model can be accomplished directly from the database via PostgreSQL LIKE queries on the JSON formatted data searching for patient/episode ID and model name.

## Internationalisation

Internationalisation is achieved using the Django/Gettext internationalisation toolchain with a few local customisations. We commit both .mo and .po files to the git repo. .po files are non-trivial to perform manual merges on via source control tooling without corrupting the files, so we would encourage only one concurrent work stream per locale.

To generate a messages file for a locale, run

`python manage.py makemessages -l $LANGUAGE_CODE`

If you have edited message files and need to compile the results, run

`python manage.py compilemessages`

To add a new locale you will need to edit the setting `LANGUAGES` to include it following the format in that tuple.

The default language is set via the LANGUAGE_CODE setting.

Most translatable strings are configured by wrapping their declaration in a gettext function call - either `_(“your string”)` in python or `{% trans “your string” %}`in templates.

Rendering translated variables in javascript rendered portions of the page (values rendered with `[[ variable ]]` syntax) can be achieved using the `translate` filter.

Our custom `makemessages` command includes translatable strings from Opal itself in the message files for this application as well as data held in lookuplist tables.

## Managing multiple customised versions

Maintaining and deploying many slightly different versions of an application is not a trivial task, and it is unlikely that any strategy can completely remove the complexity and need to think carefully when making and merging changes.

### Suggested strategy

Use master as the ‘core’ application, and then maintain a branch from that for each deployment. Using Git tags, use numbered releases on master and make merges out into each deployment branch at each tagged release. Re-tag each deployment at merge time.

### An example: minor customisation for two deployments.

First set up release tagging for your master branch.

```
git checkout master
git tag 1.0
```

Then create a deployment branch and an initial deployment branch release tag.

```
git checkout -b deployment1
git tag deployment1-1.0
```

Alter the `OPAL_BRAND_NAME` setting to include the name of the deployment.

Now alter this deployment by hide LDH: by editing form and display template.

Commit these changes and tag the deployment release.

```
git commit -a -m "Hide LDH; brand name.”
git tag deployment1-1.0.1
```

Now create a second deployment branch

```
git checkout master
git checkout -b deployment2
```

Alter the `OPAL_BRAND_NAME setting to include the name of the deployment.

then:

```
git commit -a -m "Alter brand name”
git tag deployment2-1.0.1
```

Now we will make a change to the core application.

```
git checkout master
```

Add the code `alert('HELLO WORLD THIS IS VERSION 2.0.x!’);` on the line below the code `OPAL.run(app);` in the file `entrytool/static/js/entrytool/app.js`

Now commit these changes and create a new release tag:

```
git commit -a -m “Alert everyone about the version”
git tag 2.0
```

Update our deployments to merge in the core

```
git checkout deployment1
git merge master
git tag deployment1-2.0
```

```
git checkout deployment2
git merge master
git tag deployment2-2.0
```

At deploy time, checkout the deployment version tag you want before running deployment scripts.

```
git checkout deployment2-2.0
# set up app
```
