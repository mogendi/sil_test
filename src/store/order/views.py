from order.models import Order
from order.serializer import OrderItemSerializer, OrderSerializer
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def create(self, request: Request):
        pre_validation_data = request.data.copy()
        order_serialized = OrderSerializer(data=request.data)
        order_serialized.is_valid(raise_exception=True)
        order = order_serialized.save()
        if "items" in pre_validation_data:
            for item in pre_validation_data["items"]:
                item["order"] = order.id
            item_serialized = OrderItemSerializer(
                data=pre_validation_data["items"], many=True
            )
            item_serialized.is_valid(raise_exception=True)
            item_serialized.save()

        return Response(
            data=OrderSerializer(order).data, status=status.HTTP_201_CREATED
        )
