import logging

from django.core.management import BaseCommand

from apps.middleware_counter.models import RequestLog


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--delete-all-logs",
            help="Delete all user activity logging",
            action="store_true",
        )

    def handle(self, *args, **options):
        logger = logging.getLogger("django")
        queryset = RequestLog.objects.all()
        total_deleted, details = queryset.delete()
        logger.info(f"Deleted {total_deleted} entries in the user activity log.")
