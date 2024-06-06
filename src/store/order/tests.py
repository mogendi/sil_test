import json
from unittest import mock

from customer.factories import CustomerFactory, UserFactory
from django.contrib.auth.models import User
from django.test import TransactionTestCase
from order.factories import OrderFactory
from product.factories import ProductFactory
from rest_framework.test import APIClient


class OrderCRUDTestCase(TransactionTestCase):
    client_class = APIClient

    def setUp(self) -> None:
        user: User = UserFactory.create()
        self.client.force_authenticate(user=user)

    def test_order_list(self) -> None:
        orders = OrderFactory.create_batch(size=5)
        order_ids = [str(order.id) for order in orders]

        resp = self.client.get("/orders/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(5, len(resp.json()))
        returned_ids = [order["id"] for order in resp.json()]
        for id in order_ids:
            self.assertIn(id, returned_ids)

    def test_order_read(self) -> None:
        order = OrderFactory.create()

        resp = self.client.get(f"/orders/{order.id}/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], str(order.id))

    @mock.patch("order.signals.send_conformation_sms.delay")
    def test_order_create(self, mock_send_confirmation_sms: mock.Mock) -> None:
        p1 = ProductFactory.create(price=1)
        p2 = ProductFactory.create(price=1)
        order_data = {
            "customer": str(CustomerFactory.create().pk),
            "items": [
                {"product": str(p1.pk), "amount": 1},
                {"product": str(p2.pk), "amount": 1},
            ],
        }

        resp = self.client.post(
            "/orders/",
            data=json.dumps(order_data),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 201)
        self.assertGreaterEqual(len(resp.json()["items"]), 2)
        self.assertEqual(resp.json()["total_price"], float(2))
        mock_send_confirmation_sms.assert_called()

    def test_order_update(self) -> None:
        order = OrderFactory.create()
        product_id = str(ProductFactory.create().pk)
        new_item = {"product": product_id, "amount": 1}

        resp = self.client.patch(
            f"/orders/{order.id}/",
            data=json.dumps({"items": [new_item]}),
            content_type="application/json",
        )
        self.assertEqual(resp.status_code, 200)
        returned_items = [item["product"] for item in resp.json()["items"]]
        assert product_id in returned_items

    def test_order_delete(self) -> None:
        order = OrderFactory.create()

        resp = self.client.delete(f"/orders/{order.id}/")
        self.assertEqual(resp.status_code, 204)
