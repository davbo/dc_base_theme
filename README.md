# Democracy Club Base Theme

This project contains:

* Base SCSS components, including Foundation 6 for sites
* The DC fonts
* Javascript helpers, including jQuery
* A django app containing templates and form helpers

It's designed to make managing the front end of DC projects easy and consistent

## Usage

To use this project in your django project:

`pip install git+git://github.com/DemocracyClub/dc_base_theme.git`

Add `dc_theme` to your `INSTALLED_APPS`

Configure django-pipeline in your projects `settings.py`:

```python
from dc_theme.settings import (
    get_pipeline_settings,
    STATICFILES_STORAGE,
    STATICFILES_FINDERS
)

PIPELINE = get_pipeline_settings()
```

## SCSS

To use the styles in the theme you must create a `scss` file that is findable by one of the installed `STATICFILES_FINDERS`. This is normally in an `assets` folder, or in an app's `static` folder.

This file should import the DC theme:

```css
@import 'dc_base';
```

This file then needs to be added to django-pipeline's `PIPELINE` dict. This can either be done by modifying the PIPELINE dict returned from `get_pipeline_settings`, or a list of files can be passed to that function directly:

```python
PIPELINE = get_pipeline_settings(
    extra_css=['css/styles.scss', ],
)
```

## JavaScript

Much like above, JavaScript files need to be findable by django's `STATICFILES_FINDERS`. There is no need to import the existing libraries.

Extra files can be added in the same way as CSS files:

```python
PIPELINE = get_pipeline_settings(
    extra_js=['js/scripts.js', ],
)
```

## Forms

### Template Tags


Mark up form fields in a way similar to the GDS elements by importing the `dc_forms` template tag and piping a form to it:

```
{% load dc_forms %}
{{ form|dc_form }}
```

If you like, you can also pipe a single field to this tag.

### Fields

#### DCDateField

A field that stores a date and presents 3 number input fields for day, month, year.
