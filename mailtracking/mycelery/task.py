import requests
from datetime import datetime
from celery import shared_task
from django.conf import settings
from urllib3.util.retry import Retry
from celery.utils.log import get_task_logger
from requests.adapters import HTTPAdapter

logger = get_task_logger(__name__)

@shared_task
def print_new_email_month():
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=0.5)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)

    # data = requests.get(settings.DOMAIN + "/api/v1/contacts/info/")
    data = session.get(settings.DOMAIN + "/api/v1/contacts/info/")

    logger.info("Current month: " + str(datetime.now().month) + "/" + str(datetime.now().year))
    logger.info("New email: " + data.content.decode("utf-8"))
