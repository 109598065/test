import json
import coverage
from wagtail_test.wsgi import cov
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import redirect

from django.views.static import serve
import os
filepath = 'coverage_app/coverage_data/htmlcov/'


def index(request):
    cov.html_report()
    return serve(request, os.path.basename(filepath + '/index.html'), os.path.dirname(filepath))


def object(request):
    cov.json_report()
    return JsonResponse(read_json('coverage_app/coverage_data/coverage.json'))


def reset(request):
    cov.stop()
    cov.erase()
    cov.start()
    return JsonResponse({'ok': True})


# def report_coverage():
#     cov.html_report()
#     cov.json_report()


def read_json(path):
    return json.loads(read_file(path))


def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data
