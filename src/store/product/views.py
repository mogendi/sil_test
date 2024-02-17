from product.models import Product
from product.serializers import ProductSerializer
from rest_framework.viewsets import ModelViewSet


class ProductViewset(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
