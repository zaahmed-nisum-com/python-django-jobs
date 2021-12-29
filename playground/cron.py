from django.shortcuts import render
import logging
logger = logging.getLogger('django')

def cron_job_file():
    f =open('/Users/zahmed 1/Desktop/pythoncronjob/pythontextfile_1.txt','w')
    f.write("Now the file has more content!")
    f.close()