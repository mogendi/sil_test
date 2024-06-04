from core.db import BaseModel
from customer.models import Customer
from django.db import models
from product.models import Product


class Order(BaseModel):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class OrderItems(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, related_name="orderitems", on_delete=models.CASCADE
    )
    amount = models.IntegerField()
