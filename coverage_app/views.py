import json
import coverage
from myproject.wsgi import cov
# from django.http import HttpResponse
from django.http import JsonResponse


def index(request):
    report_coverage()
    return JsonResponse(read_json('coverage/coverage.json'))


def reset(request):
    cov.stop()
    cov.erase()
    cov.start()
    return JsonResponse({'ok': True})


def report_coverage():
    # cov.html_report()
    cov.json_report()


def read_json(path):
    return json.loads(read_file(path))


def read_file(path):
    file = open(path, "r")
    data = file.read()
    file.close()
    return data
