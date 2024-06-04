from product.models import Product
from product.serializers import ProductSerializer
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated]
