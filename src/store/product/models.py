from core.db import BaseModel
from core.utils import generate_product_code
from django.db import models


class Product(BaseModel):
    code = models.CharField(
        default=generate_product_code, editable=False, max_length=255
    )
    name = models.CharField(max_length=255)
    price = models.FloatField()
