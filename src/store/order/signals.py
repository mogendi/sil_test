from typing import Type

from django.db import transaction
from django.db.models import Model
from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from order.tasks import send_conformation_sms


@receiver(post_save, sender=Order)
def send_notification_on_forum_create(
    sender: Type[Model], instance: Order, created, **kwargs
) -> None:
    if created:
        transaction.on_commit(
            lambda: send_conformation_sms.delay(
                instance.customer_id,
                f"Your order has been confirmed! Order number {instance.id}",
            )
        )
