from customer.models import Customer
from customer.serilizer import CustomerSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class CustomerViewset(ModelViewSet):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    permission_classes = [permissions.IsAuthenticated]
