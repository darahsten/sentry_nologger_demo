New Sentry SDK Logger.exception failure Demo
============================================

A project to demo failure of logger.exception to sent to sentry in new sentry sdk

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT

Introduction
------------
The new sentry sdk (DSN) introduces some incompatibilities with raven and hence required.
Documentation on how to upgrade to the new sentry sdk is lacking for django projects.

I wanted to upgrade and discovered along the way that logger.exception(repr(e)) no longer
sends any errors to sentry when using the new dsn.

See more here https://stackoverflow.com/questions/57274935/configuring-sentry-handler-for-django-with-new-sentry-sdk-without-raven/57294650#57294650

This is a simple project to demo that behavior in response to the comments.


SETUP
-----

Configured using sqlite (no need for postgres).

setup a virtualenv mkvirtualenv sentry_nologger_demo
workon on sentry_nologger_demo

pip install -r requirements.txt

python manage.py runserver --settings=config.settings

Ensure that you have a .env file with environment variable DJANGO_SENTRY_DSN=project_sentry_dsn in
the new format i.e. without the secret key

To test navigate to localhost:8000/sentry-debug/  >>>> Tells you, you are logging to sentry correctly. Will throwup an exception in template
Navigate to localhost:8000/sentry-logs-error/ >>>> using capture exception to log the error, You should see this in sentry
Navigate to localhost:8000/sentry-nologs-error/ >>>>>> trying logger.exception, never logs anything to sentry. This will only appear in console

All the demo pages are in config.urls FYI.
If I made a mistake in the setup please let me know.


