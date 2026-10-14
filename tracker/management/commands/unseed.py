from django.core.management.base import BaseCommand

from tracker.models import Request


class Command(BaseCommand):
    help = 'Delete all maintenance requests.'

    def handle(self, *args, **options):
        deleted, _ = Request.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f'Deleted {deleted} requests.'))
