import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
        with open("/Users/karramba/Library/Group Containers/UBF8T346G9.Office/SolutionPackages/7da11070ccfbf177cfa6df777d2e3c9c/PackageResources/catalog.json", encoding="utf-8") as file:
            data = json.load(file)
        for category in data:
            if category['model'] == "catalog.category":
                return category

    @staticmethod
    def json_read_products():
        with open("/Users/karramba/Library/Group Containers/UBF8T346G9.Office/SolutionPackages/7da11070ccfbf177cfa6df777d2e3c9c/PackageResources/catalog.json", encoding='utf-8') as file:
            data = json.load(file)
        for product in data:
            if product['model'] == 'catalog.product':
                return product


    def handle(self, *args, **options):

        Category.objects.all().delete()
        Product.objects.all().delete()

        product_for_create = []
        category_for_create = []

        for category in Command.json_read_categories():
            category_for_create.append(Category(**category))

        Category.objects.bulk_create(category_for_create)

        for product in Command.json_read_products():
            product_for_create.append(Product(**product))

        Product.objects.bulk_create(product_for_create)