from order.models import Order
from order.serializer import OrderItemSerializer, OrderSerializer
from order.tasks import send_conformation_sms
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related("orderitems").all()

    def create(self, request: Request):
        pre_validation_data = request.data.copy()
        order_serialized = OrderSerializer(data=request.data)
        order_serialized.is_valid(raise_exception=True)
        order: Order = order_serialized.save()
        if "items" in pre_validation_data:
            for item in pre_validation_data["items"]:
                item["order"] = order.id
            item_serialized = OrderItemSerializer(
                data=pre_validation_data["items"], many=True
            )
            item_serialized.is_valid(raise_exception=True)
            item_serialized.save()

        send_conformation_sms.delay(
            order.customer_id,
            f"Your order has been confirmed! Order number {order.id}",
        )

        return Response(
            data=OrderSerializer(order).data, status=status.HTTP_201_CREATED
        )
