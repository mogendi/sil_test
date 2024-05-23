from unittest import mock

from customer.factories import CustomerFactory
from order.factories import OrderFactory
from product.factories import ProductFactory
from rest_framework.test import APITestCase


class orderCRUDTestCase(APITestCase):
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

    @mock.patch("order.tasks.send_conformation_sms.delay")
    def test_order_create(self, mock_send_confirmation_sms: mock.Mock) -> None:
        order_data = {
            "customer": CustomerFactory.create().pk,
            "items": [
                {"product": ProductFactory.create().pk},
                {"product": ProductFactory.create().pk},
            ],
        }

        resp = self.client.post("/orders/", data=order_data, format="json")
        self.assertEqual(resp.status_code, 201)
        self.assertGreaterEqual(len(resp.json()["items"]), 2)
        mock_send_confirmation_sms.assert_called()

    def test_order_update(self) -> None:
        order = OrderFactory.create()
        new_item = {"product": ProductFactory.create().pk}

        resp = self.client.patch(
            f"/orders/{order.id}/", data={"items": new_item}, format="json"
        )
        self.assertEqual(resp.status_code, 200)

    def test_order_delete(self) -> None:
        order = OrderFactory.create()

        resp = self.client.delete(f"/orders/{order.id}/")
        self.assertEqual(resp.status_code, 204)
