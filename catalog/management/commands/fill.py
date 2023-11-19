from django.core.management import BaseCommand

from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {'name_product': 'Яблоко', 'description': 'Зеленое', 'category': '2', 'price': '100'},
            {'name_product': 'Морковь', 'description': 'Оранжевая', 'category': '1', 'price': '30'},
            {'name_product': 'Банан', 'description': 'Из Эквадора', 'category': '2', 'price': '100'}

        ]

        products_for_create = []
        for product in product_list:
            category_id = product.pop('category')
            category = Category.objects.get(id=category_id)
            product['category'] = category
            products_for_create.append(Product(**product))
        Product.objects.bulk_create(products_for_create)

