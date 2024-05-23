from core.db import BaseModel
from core.utils import generate_customer_code
from django.db import models


class Customer(BaseModel):
    name = models.CharField(max_length=255)
    code = models.CharField(
        default=generate_customer_code, editable=False, max_length=255
    )
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
