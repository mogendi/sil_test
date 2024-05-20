import factory
from customer.models import Customer


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker("sentence", nb_words=2)
    location = factory.Faker("sentence", nb_words=2)
