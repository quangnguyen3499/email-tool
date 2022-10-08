from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

def send_mail_statistic_service(*, email: str, statistic: object):
    subject = "Monthly Statistic Email"
    body = render_to_string("email_statistic.html", {
        "time": statistic["time"],
        "new_this_month": statistic["new_email_this_month"],
        "count": statistic["count"],
        "unsubscribed": statistic["unsubscribed"],
    })
    to = [email]
    send_mail(
        subject=subject,
        message="",
        html_message=body,
        from_email=settings.SELLER_EMAIL,
        recipient_list=to,
    )
