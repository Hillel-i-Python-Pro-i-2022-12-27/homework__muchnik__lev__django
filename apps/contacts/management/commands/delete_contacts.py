import logging

from django.core.management.base import BaseCommand

from apps.contacts.models import Contact


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--is-only-auto-generated",
            help="Delete only auto generated contacts?",
            action="store_true",
        )

    def handle(self, *args, **options):
        is_only_auto_generated: bool = options["is_only_auto_generated"]
        logger = logging.getLogger("django")

        queryset = Contact.objects.all()

        logger.info(f"Current amount of contacts before: {queryset.count()}")
        if is_only_auto_generated:
            queryset.filter(is_auto_generated=True)
        total_deleted, details = queryset.delete()

        logger.info(f"Total deleted: {total_deleted}, details: {details}")
