from django.shortcuts import render
from django.http import HttpResponse
from  playground.cron  import cron_job
import logging
logger = logging.getLogger('django')

# Create your views here.

async def say_hello(request):
    logger.info('logging testing')
    r = await cron_job()
    print(r)
    if r == 1:
        return HttpResponse('hello world')