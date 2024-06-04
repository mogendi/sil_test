from order.models import Order, OrderItems
from order.serializer import OrderItemSerializer, OrderSerializer
from rest_framework import permissions, status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class OrderViewset(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.prefetch_related("orderitems").all()
    permission_classes = [permissions.IsAuthenticated]

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

        return Response(
            data=OrderSerializer(order).data, status=status.HTTP_201_CREATED
        )

    def update(self, request, pk: str, **kwargs):
        items = []
        order = Order.objects.get(pk=pk)
        OrderItems.objects.filter(order=order).delete()
        if "items" in request.data:
            for item in request.data["items"]:
                item["order"] = pk
            item_serialized = OrderItemSerializer(
                data=request.data["items"],
                many=True,
            )
            item_serialized.is_valid(raise_exception=True)
            items = item_serialized.save()
            order.orderitems.set(items)
        return super().update(request, pk, **kwargs)
