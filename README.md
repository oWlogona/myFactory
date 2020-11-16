####Нужно обновить приложения products. А именно добавить возможно создание новой категории для товаров, так же должна быть возможно создавать товары в каждой категории.
У товара должны быть такие поля:
* name
* brand
* price
* width
* height

Следует помнить что ** **brand** ** может быть общий у нескольких товаров.

У нас есть 2 templates:
- Видими все бренды c их товарами, а так же можем создать новый. Для этого передаем response и form:
```bigquery 
{
    "samsung": [
        {
            "name": "A10",
            "brand": "samsung",
            "price": 1000,
            "width": "10",
            "height": "20"
        },
        {
            "name": "A20",
            "brand": "samsung",
            "price": 120,
            "width": "10",
            "height": "20"
        }
    ],
    "apple": [
        {
            "name": "IMAC",
            "brand": "iphone",
            "price": 10000,
            "width": "100",
            "height": "200"
        }
    ]
}
```
- Видим выбранный бренд и его товары, есть возможность создать новый товар. Для этого передаем response and form
```bigquery 
{
    "name": "samsung",
    "data": [
        {
            "name": "A10",
            "brand": "samsung",
            "price": 1000,
            "width": "10",
            "height": "20"
        },
        {
            "name": "A20",
            "brand": "samsung",
            "price": 120,
            "width": "10",
            "height": "20"
        }
    ],
}
```