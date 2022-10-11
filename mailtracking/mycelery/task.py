import json
import requests
import threading
from celery import shared_task
from django.conf import settings
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from celery.utils.log import get_task_logger
from .services import send_mail_statistic_service

logger = get_task_logger(__name__)

@shared_task
def print_new_email_month():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    
    data = json.loads(session.get(settings.DOMAIN + "/api/v1/contacts/info/").content.decode("utf-8")["data"])

    logger.info(data)
    t = threading.Thread(
            target=send_mail_statistic_service(
                email=settings.SELLER_EMAIL,
                statistic=data,
            ),
            args=(3,),
        )
    t.start()
    t.join()

    logger.info("Current month: " + data["time"])
    logger.info("New email: " + str(data["new_email_this_month"]))
