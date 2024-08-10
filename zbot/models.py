from django.db import models

class MLModelPrediction(models.Model):
    ticker = models.CharField(max_length=10)
    date = models.DateField()
    prediction = models.CharField(max_length=10)  # 'BUY', 'SELL', or 'HOLD'
    actual = models.CharField(max_length=10)  # Actual outcome for evaluation


class FinancialData(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    volume = models.IntegerField()
    ticker = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.ticker} - {self.date}"


