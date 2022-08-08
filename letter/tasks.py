from datetime import datetime

from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from django.conf import settings

from .models import Letter


logger = get_task_logger(__name__)

@shared_task(name='Send-emails')
def send_email():
    logger.info('Checking for emails ready to be delivered today')
    logger.info('Please wait...')
    count: int = 0 
    today = datetime.today().date()
    for letter in Letter.objects.all():
        if letter.date == today and letter.delivered == False:
            count += 1
    if count:
        logger.info(f'Found {count} email(s) to be delivered')
        logger.info('Delivering emails...')
        for letter in Letter.objects.all():
            if letter.date == today and letter.delivered == False:
                status: int = send_mail(
                    letter.title,
                    letter.message,
                    settings.DEFAULT_FROM_EMAIL,
                    [letter.email_address],
                )
                if status == 1:
                    letter.delivered = True
                    letter.save()
        logger.info(f'{count} email(s) delivered successfully')
    else:
        logger.info('No email(s) to be delivered today.')
    
