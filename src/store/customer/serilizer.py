from customer.models import Customer
from rest_framework.serializers import ModelSerializer


class CustomerSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Customer
