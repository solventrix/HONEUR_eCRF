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

You can create an initial user using the `create opalsuperuser` management
command noted in the installation section.

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

Where installations are expected to include the load of initial data via file
upload, it may be useful to consider the configuration of timeout parameters
for both web and application servers.

This functionality currently processes data uploads in a HTTP request, for
large files this may exceed the default process timeout for either http or
application server.

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

Adding an entirely new set of data will require creating a new model in `entrytool.models.py`. This is a python class the inherits from `opal.models.EpisodeSubrecord` that generates a new table in the database. This process is documented extensively by Django, Opal specific alterations (mostly additional properties that are available) are documented in the Opal documentation, and the models `SCT`, `Regimen`, and `Response provide examples within this application.

Once the model is created the database needs to be updated:

1. `python manage.py makemigrations`
2. `python manage.py migrate`

We can then create form and display templates for this model by running `python manage.py scaffold entrytool` this will create the templates in `entrytool/templates/records/$MODELNAME.html` and `entrytool/templates/forms/$MODELNAME_form.html`. These can be edited to adjust widgets in use, or refine the layout of individual records. The other templates in the folders `entrytool/templates/records/` and `entrytool/templates/forms` should serve as an example of how these can be adjusted.

The new model will then need to be added to the line of treatment template at
`entrytool/templates/detail/treatmentline.html` with a new record panel declaration
`{% record_panel models.$MODELNAME %}`. The location of this panel relative to the
others can be adjusted by editing this template’s layout as defined by the Bootstrap
css classes e.g. `row` and `col-md$X`. The bootstrap website has extensive
documentation for creating layouts using these classes, and this application contains
many examples.

## Data Validation

Data validation is defined as a set of validation rules in javascript.
These are found in the file `entrytool/templates/validation_rules.js`

This Angular service returns an object that maps fields in the application
to javascript functions and error messages to display when validation is failed.

For example, the validation for `entrytool.models.PatientStatus` reads as follows:

```javascript
patient_status: {
    death_date: {
        errors: [
	    [Validators.afterDateOfBirth,  "{% trans "Date of death is before the date of birth" %}"],
	    [Validators.noFuture, "{% trans "Date of death cannot be in the future" %}"]
		]
	},
    death_cause: {
	errors: [
            [Validators.inOptions, "{% trans "is not in the options available" %}"]
		]
	}
}
```

This architecture allows us to define validation once, and use it for both
validating data loaded from file, and data in forms.

A number of reusable validation functions have been written in the service
`Validators`, but it is also possible to write any arbitrary code for more
esoteric requirements.

The implementation of these validators can be reviewed at
`entrytool/static/js/services/validators.js`

### Required fields

`Validators.required` will ensure that this field is entered.

### Maximum length

For character fields, `Validators.maxLength(255)` would ensure a maximum lentgth
of 255 characters.

### Categorical variables

`Validators.inOptions` requires a value to be in the values declared by the field,
whether this is using Django choices, or a lookuplist. This is useful for data
imported from file that may not have these exact values.

### Relative date validation

We sometimes wish to validate that a date is before, or after another date.

`Validators.aferDateOfBirth` will raise a validation error if the date this
validator is declared against is after the date of birth for this patient.

`Validators.noFuture` ensures that the value of a field is not greater than
the current date - for instance a date of death should not be in the future.


## Batch Imports

Imports from file are supported via an upload page in the application.

Thus far there is no known standardised file format for importing data.

Accordingly we have implemented an API for receiving files to process and
returning error information to the user, and some example importers without
attempting to define a formal importer API.

The setting `UPLOAD_FROM_FILE_FUNCTION` refers to a callable that takes
a file like object and returns error information that is displayed by
the UI.

This information is contained within a datastructue as follows:

```
{
    # Errors related to the files themselves e.g. Not a zipfile / encoding / missing files
    "top_level_errors": ["Strings containing errors", "These should not be related to data"],

    # Errors about individual data points in the uploaded data
    "row_errors":[

       "file" : "name_of_the_file_data_is_in.csv",
       "row"  : 3, # Row on which the data in question is located
       "value": "?", # The value in question at this cell
       "column": "date_of_death", # The header row of this column
       "short_description", "? Is not a date", # The problem with this cell
       "traceback" "..." # The full python traceback for this error
    ]
}
```

## Customisation of search results

Search results are generated by passing the search string as a query to a list of predefined database fields. These can be adjusted by changing the setting `OPAL_SEARCH_FIELDS`. The syntax for this list of fields matches that of the (Django Queryset)[https://docs.djangoproject.com/en/3.1/ref/models/querysets/#queryset-api] API. The fields in this setting will be used as arguments to a filter query on the Patient model.

## Unit tests
Opal ships with a test runner that will run both python and javascript unit tests.
Details including installlation details can be found on the (opal test documentation page)[https://opal.openhealthcare.org.uk/docs/reference/testing/]. After the required libraries have been installed unit tests can be run with `opal test`

This project includes both javascript and python unit tests and especially when moving into a world with multiple forks it is recommended that these are used to ensure functionality.


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

`python manage.py makemessages --extension=js,py,html -l $LANGUAGE_CODE`

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
