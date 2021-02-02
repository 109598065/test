"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
###########
import coverage, atexit
cov = coverage.Coverage(config_file='coverage_app/coverage_data/.coveragerc')
cov.start()
###########
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

application = get_wsgi_application()

###########
def save_coverage():
    cov.stop()
#     cov.html_report()
#     cov.json_report()

atexit.register(save_coverage)
###########