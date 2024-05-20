import factory
from customer.factories import CustomerFactory
from order.models import Order, OrderItems
from product.factories import ProductFactory


class OrderFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Order

    customer = factory.SubFactory(CustomerFactory)

    @factory.post_generation
    def items(self, create, extracted, **kwargs) -> None:
        if create:
            order_items = OrderItemFactory.create_batch(size=2, order=self)
            for item in order_items:
                self.orderitems.add(item)


class OrderItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = OrderItems

    product = factory.SubFactory(ProductFactory)
    order = factory.SubFactory(OrderFactory)
