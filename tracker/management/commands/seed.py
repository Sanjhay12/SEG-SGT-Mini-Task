import random

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from tracker.models import Request

PROBLEMS = [
    'Leaking tap', 'Broken light fitting', 'Blocked drain', 'Faulty radiator', 'Door won\'t lock',
    'Cracked window', 'Flickering lights', 'No hot water', 'Damp patch on ceiling', 'Broken blind',
    'Jammed fire door', 'Noisy air conditioning', 'Toilet won\'t flush', 'Loose handrail',
    'Power socket not working', 'Lift out of service', 'Broken chair', 'Mould in corner',
    'Smoke alarm beeping', 'Damaged floor tiles',
]
LOCATIONS = [
    'Room 101', 'Room 204', 'Main reception', 'Library', 'Staff kitchen', 'Ground floor toilets',
    'Lecture theatre 2', 'Meeting room B', 'Stairwell C', 'Car park', 'Server room', 'Cafeteria',
    'Second floor corridor', 'Lab 3', 'Gym changing room',
]
DETAILS = [
    'Reported by several people this week.',
    'This has been getting worse over the past few days.',
    'Please attend as soon as possible.',
    'Not urgent, but should be fixed before the end of the month.',
    'A temporary fix was applied previously but the problem has returned.',
    'Area has been cordoned off for safety.',
    'Happens mostly in the mornings.',
    'Photos available on request.',
]


class Command(BaseCommand):
    help = 'Create sample maintenance requests.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--count',
            type=int,
            default=settings.SEED_REQUEST_COUNT,
            help=f'Number of requests to create (default: {settings.SEED_REQUEST_COUNT}).',
        )

    def handle(self, *args, count, **options):
        if count < 0:
            raise CommandError('--count cannot be negative.')
        requests = []
        for _ in range(count):
            problem, location = random.choice(PROBLEMS), random.choice(LOCATIONS)
            details = ' '.join(random.sample(DETAILS, k=random.randint(1, 3)))
            description = f'{problem} reported in {location}. {details}'
            requests.append(Request(title=f'{problem} – {location}', description=description))
        Request.objects.bulk_create(requests)
        self.stdout.write(self.style.SUCCESS(f'Created {count} requests.'))
