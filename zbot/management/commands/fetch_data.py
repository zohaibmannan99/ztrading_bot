import yfinance as yf
from django.core.management.base import BaseCommand
from zbot.models import FinancialData

class Command(BaseCommand):
    help = 'Fetch financial data and store in database'

    def handle(self, *args, **kwargs):
        ticker = "AAPL"
        start_date = "2020-01-01"
        end_date = "2021-01-01"
        data = yf.download(ticker, start=start_date, end=end_date)

        for index, row in data.iterrows():
            FinancialData.objects.create(
                date=index,
                open=row['Open'],
                high=row['High'],
                low=row['Low'],
                close=row['Close'],
                volume=row['Volume'],
                ticker=ticker
            )
        self.stdout.write(self.style.SUCCESS('Successfully fetched and stored data'))
