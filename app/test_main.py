import datetime
import pytest
from app.main import outdated_products


@pytest.mark.parametrize(
    "products, expected", [
        (
            [
                {
                    "name": "salmon",
                    "expiration_date": datetime.date(2024, 10, 10),
                    "price": 600
                },
                {
                    "name": "chicken",
                    "expiration_date": datetime.date(2024, 9, 5),
                    "price": 120
                },
                {
                    "name": "duck",
                    "expiration_date": datetime.date(2024, 8, 1),
                    "price": 160
                }
            ],
            [
                "duck"
            ]
        )
    ]
)
def test_outdated_products(
        products: list,
        expected: list
) -> None:
    result = outdated_products(products)
    assert result == expected
