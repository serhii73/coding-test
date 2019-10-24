# Task 2 - Scraping

In this task you're going to build a function that takes a url as input and returns a list of products.
The url to be scraped is [http://books.toscrape.com/index.html](http://books.toscrape.com/index.html).

Each product should contain the following attributes: name, price, image, rating, in_stock.

## Example response:
```
[
    {
        'image': 'http://books.toscrape.com/media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg',
        'in_stock': True,
        'name': 'A Light in the ...',
        'price': '£51.77',
        'rating': 3
    },
    ...
]
```

## Project setup

Write your solution in task.py

Write your test code in test.py

Project package requirements can be found in requirements.txt
