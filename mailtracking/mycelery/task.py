from celery import shared_task
from celery.utils.log import get_task_logger
import requests
from datetime import datetime

logger = get_task_logger(__name__)

@shared_task
def print_new_email_month():
    data = requests.get("http://localhost:8000/api/v1/contacts/info/")
    logger.info("Current month: " + str(datetime.now().month) + "/" + str(datetime.now().year))
    logger.info("New email: " + data.content.decode("utf-8"))
