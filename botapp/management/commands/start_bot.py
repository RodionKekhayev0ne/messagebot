# mybot/management/commands/start_bot.py
from django.core.management.base import BaseCommand
from botapp.bot import start_bot


class Command(BaseCommand):
    help = 'Запускает Telegram бота'

    def handle(self, *args, **kwargs):
        import asyncio
        asyncio.run(start_bot())
