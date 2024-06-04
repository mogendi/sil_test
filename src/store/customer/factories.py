import factory
from customer.models import Customer
from django.contrib.auth.models import User


class CustomerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Customer

    name = factory.Faker("sentence", nb_words=2)
    location = factory.Faker("sentence", nb_words=2)
    phone_number = factory.Faker("sentence", nb_words=1)


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        exclude = ("new_user",)

    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "password")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
