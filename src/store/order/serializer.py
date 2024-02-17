from order.models import Order, OrderItems
from rest_framework import serializers


class OrderSerializer(serializers.ModelSerializer):
    items = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Order

    def get_items(self, obj: Order) -> "OrderItemSerializer":
        return [OrderItemSerializer(item).data for item in obj.items]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = OrderItems
