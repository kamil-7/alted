from django.core.management import BaseCommand
from django.db.utils import IntegrityError
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from alted.management.commands.initialize_admin import initialize_admin
from alted.taskapp.update_exchange_rates import update_exchange_rates
from alted.taskapp.update import update
from alted.taskapp.update_market_list import update_market_list
from alted.taskapp.exchanges.update_ticker_url import update_ticker_url
from coins.models import Coin
from exchanges.models import Exchange
from markets.models import Market
from users.models import User

EXCHANGES = (
    ('PLNX', 'Poloniex'),
    ('BTRX', 'Bittrex'),
    ('BITM', 'Bitmarket'),
    ('BITB', 'Bitbay'),
    ('BITMS', 'Bitmaszyna')
)


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.stdout.write('(1/4) Filling database with initial data')

        Exchange.objects.get_or_create(code='BTFX', name='Bitfinex', code_substitutes=dict(
            QTUM='qtm',
            DASH='dsh'
        ))

        for code, name in EXCHANGES:
            Exchange.objects.get_or_create(code=code, name=name)

        self.stdout.write('(2/4) Creating superuser')

        email = 'admin@mail.com'
        password = 'pass'

        try:
            User.objects.create_superuser(email, password)
        except IntegrityError:
            user = User.objects.get(email=email)
            user.is_staff = True
            user.is_superuser = True
            user.save()

        self.stdout.write('Created superuser with email {} and password {}.'.format(email, password))

        self.stdout.write('(3/4) Pulling data from API')

        update_ticker_url()
        update_market_list(force_coins=True)

        fiat = Coin.objects.get(code='USD')
        coin = Coin.objects.get(code='USDT')
        coin.tethered_fiat = fiat
        coin.save()

        update_exchange_rates()
        update()

        self.stdout.write('(4/4) Adding periodic tasks to database')

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=1,
            period=IntervalSchedule.MINUTES
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Update',
            task='alted.taskapp.update.update'
        )

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=60,
            period=IntervalSchedule.MINUTES
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Update market list',
            task='alted.taskapp.update_market_list.update_market_list'
        )

        schedule, created = IntervalSchedule.objects.get_or_create(
            every=45,
            period=IntervalSchedule.MINUTES
        )

        PeriodicTask.objects.get_or_create(
            interval=schedule,
            name='Update exchange rates',
            task='alted.taskapp.update_exchange_rates.update_exchange_rates'
        )

        initialize_admin()

        self.stdout.write(self.style.SUCCESS('Database initialization complete'))
