import requests
from bs4 import BeautifulSoup
from word2number import w2n


def get_products_from_page(url):
    """Return data from all books."""

    def get_data_from_book(book):
        """Return data from one book."""
        src_img = book.find("img").get("src")
        src_img = src_img.replace("../", "")
        image = "http://books.toscrape.com/" + src_img

        in_stock = False
        in_stock_or_not = book.find("p", {"class", "instock"}).text
        if "In stock" in in_stock_or_not:
            in_stock = True

        name = book.find("h3").find("a").text

        price = book.find("p", {"class", "price_color"}).text
        price = price.replace("Â", "")

        rating = book.find("p", {"class", "star-rating"}).get("class")[1]
        rating = w2n.word_to_num(rating)

        return {
            "image": image,
            "in_stock": in_stock,
            "name": name,
            "price": price,
            "rating": rating,
        }

    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    books = soup.find_all("article", {"class", "product_pod"})

    result = list(map(get_data_from_book, books))
    return result
