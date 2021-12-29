from django.shortcuts import render
from django.http import HttpResponse
from  playground.cron  import cron_job,cron_job_file
import logging
logger = logging.getLogger('django')

# Create your views here.

def say_hello(request):
    cron_job_file()
    return HttpResponse('hello world')