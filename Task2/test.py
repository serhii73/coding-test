import pytest

from .task import get_products_from_page

result_page_2 = get_products_from_page(
    "http://books.toscrape.com/catalogue/page-2.html"
)
result_page_1 = get_products_from_page("http://books.toscrape.com/index.html")


def test_get_products_from_page():
    assert result_page_2[0] == {
        "image": "http://books.toscrape.com/media/cache/5d/72/5d72709c6a7a9584a4d1cf07648bfce1.jpg",
        "in_stock": True,
        "name": "In Her Wake",
        "price": "£12.84",
        "rating": 1,
    }
    assert result_page_1[0] == {
        "image": "http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg",
        "in_stock": True,
        "name": "A Light in the ...",
        "price": "£51.77",
        "rating": 3,
    }
    assert result_page_1[1] == {
        "image": "http://books.toscrape.com/media/cache/26/0c/260c6ae16bce31c8f8c95daddd9f4a1c.jpg",
        "in_stock": True,
        "name": "Tipping the Velvet",
        "price": "£53.74",
        "rating": 1,
    }
