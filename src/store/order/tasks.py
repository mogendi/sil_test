from celery_conf import app as celery_app
from customer.models import Customer

from src.utils.at import at_util


@celery_app.task(
    name=__name__ + ".send_conformation_sms",
    queue="notifications-q",
)
def send_conformation_sms(customer_id, message: str) -> None:
    customer = Customer.objects.get(id=customer_id)
    at_util.send(message=message, numbers=[customer.phone_number])
