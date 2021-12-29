from django.shortcuts import render
import logging
logger = logging.getLogger('django')


async def cron_job():
    print('zain ahmed')
    logger.info('job called')
    return  1