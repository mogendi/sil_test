import random
import string

from product.factories import ProductFactory
from rest_framework.test import APITestCase


class ProductCRUDTestCase(APITestCase):
    def test_product_list(self) -> None:
        products = ProductFactory.create_batch(size=5)
        product_ids = [str(product.id) for product in products]

        resp = self.client.get("/products/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(5, len(resp.json()))
        returned_ids = [product["id"] for product in resp.json()]
        for id in product_ids:
            self.assertIn(id, returned_ids)

    def test_product_read(self) -> None:
        product = ProductFactory.create()

        resp = self.client.get(f"/products/{product.id}/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["id"], str(product.id))

    def test_product_create(self) -> None:
        name = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        price = random.uniform(1.0, 1000.0)
        product_data = {"name": name, "price": price}

        resp = self.client.post("/products/", data=product_data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.json()["name"], name)
        self.assertEqual(resp.json()["price"], price)

    def test_product_update(self) -> None:
        product = ProductFactory.create()
        old_name = product.name
        new_name = "".join(
            random.choices(string.ascii_uppercase + string.digits, k=10)
        )  # noqa :E501
        assert old_name != new_name

        resp = self.client.patch(
            f"/products/{product.id}/", data={"name": new_name}
        )  # noqa :E501
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()["name"], new_name)

    def test_product_delete(self) -> None:
        product = ProductFactory.create()

        resp = self.client.delete(f"/products/{product.id}/")
        self.assertEqual(resp.status_code, 204)
