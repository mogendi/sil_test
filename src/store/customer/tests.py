import random
import string

from customer.factories import CustomerFactory
from rest_framework.test import APITestCase


class CustomerCRUDTestCase(APITestCase):
    def test_customer_list(self) -> None:
        customers = CustomerFactory.create_batch(size=5)
        customer_ids = [str(customer.id) for customer in customers]

        resp = self.client.get("/customers/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(5, len(resp.json()))
        returned_ids = [customer["id"] for customer in resp.json()]
        for id in customer_ids:
            self.assertIn(id, returned_ids)

    def test_customer_read(self) -> None:
        customer = CustomerFactory.create()

        resp = self.client.get(f"/customers/{customer.id}/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], str(customer.id))

    def test_customer_create(self) -> None:
        name = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        location = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        phone_number = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        customer_data = {
            "name": name,
            "location": location,
            "phone_number": phone_number,
        }

        resp = self.client.post("/customers/", data=customer_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["name"], name)
        self.assertEqual(resp.json()["location"], location)

    def test_customer_update(self) -> None:
        customer = CustomerFactory.create()
        old_name = customer.name
        new_name = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        assert old_name != new_name

        resp = self.client.patch(
            f"/customers/{customer.id}/", data={"name": new_name}
        )  # noqa :E501
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["name"], new_name)

    def test_customer_delete(self) -> None:
        customer = CustomerFactory.create()

        resp = self.client.delete(f"/customers/{customer.id}/")
        self.assertEqual(resp.status_code, 204)
