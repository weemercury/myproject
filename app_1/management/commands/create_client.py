from django.core.management.base import BaseCommand
from app_1.models import Client


class Command(BaseCommand):
    help = "Create client."
    def handle(self, *args, **kwargs):
        client = Client(
            name='Alex', 
            email='alex@example.com',
            phone_number = 89191118899, 
            address = 'Moscow',
            registration_date = '2023-12-01')
        client.save()
        self.stdout.write(f'{client}')