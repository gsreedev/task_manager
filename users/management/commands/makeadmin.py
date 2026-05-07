from django.core.management.base import BaseCommand, CommandError
from users.models import User

class Command(BaseCommand):
    help = 'Promotes a given user to an Admin (superuser)'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='The username of the user to promote')

    def handle(self, *args, **options):
        username = options['username']
        
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise CommandError(f'User "{username}" does not exist.')

        if user.is_superuser:
            self.stdout.write(self.style.WARNING(f'User "{username}" is already an Admin.'))
            return

        user.is_superuser = True
        user.is_staff = True
        user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully promoted user "{username}" to Admin.'))
