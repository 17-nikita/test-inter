import csv
from django.core.management.base import BaseCommand
from testing.models import Product
from datetime import datetime

class Command(BaseCommand):
    help = 'Bulk import CSV data'

    def handle(self, *args, **kwargs):
        objects = []

        with open('import.csv', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                created_at = datetime.fromisoformat(row['created_at'])
                objects.append(
                    Product(
                        name=row['name'],
                        category=row['category'],
                        price=row['price'],
                        stock=row['stock'],
                        created_at=created_at,
                    )
                )

        Product.objects.bulk_create(objects, batch_size=1000)

        self.stdout.write(self.style.SUCCESS('Bulk insert completed!'))