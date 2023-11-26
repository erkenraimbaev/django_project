from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Category.objects.all().delete()
        category_list = [
            {'name_category': 'Овощи', 'description': 'Едят все'},
            {'name_category': 'Фрукты', 'description': 'Очень полезны'}
        ]
        Category.truncate_table_restart_id()
        for category in category_list:
            Category.objects.create(**category)

        product_list = [
            {'name_product': 'Яблоко', 'description': 'Зеленое', 'image': 'media/catalog/яблоко.jpg', 'category': '2', 'price': '100'},
            {'name_product': 'Морковь', 'description': 'Оранжевая', 'image': 'media/catalog/морковь.jpg', 'category': '1', 'price': '30'},
            {'name_product': 'Банан', 'description': 'Из Эквадора', 'image': 'media/catalog/банан.jpg', 'category': '2', 'price': '100'}
        ]

        products_for_create = []
        Product.truncate_table_restart_id()
        for product in product_list:
            category_id = product.pop('category')
            products_for_create.append(Product(category_id=category_id, **product))
        Product.objects.bulk_create(products_for_create)
