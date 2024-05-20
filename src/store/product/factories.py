import factory
from product.models import Product


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.Faker("sentence", nb_words=2)
    price = factory.Faker("pyfloat")
