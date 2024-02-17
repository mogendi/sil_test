import random
import string


def random_string(len: int = 10) -> str:
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(len))


def generate_customer_code() -> str:
    return f"cstmr-{random_string(4)}".upper()


def generate_product_code() -> str:
    return f"prdct-{random_string(4)}".upper()
