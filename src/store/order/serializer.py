from typing import List

from order.models import Order, OrderItems
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Order

    def get_items(self, obj: Order) -> "List[OrderItemSerializer]":
        return [
            OrderItemSerializer(item).data for item in obj.orderitems.all()
        ]  # noqa: E501


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = OrderItems
