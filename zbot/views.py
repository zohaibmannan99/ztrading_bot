from django.shortcuts import render
from django.urls import path
from django.http import JsonResponse
from zbot.models import FinancialData
from django.http import HttpResponse
from zbot import views
import json
from .ml_model import train_ml_model
from .ml_model import make_prediction


def index(request):
    return render(request, 'zbot/index.html')


def predict(request):
    if request.method == 'POST':
        ticker = json.loads(request.body)
        data = FinancialData.objects.filter(ticker=ticker).order_by('date')
        # Fetch financial data and make a prediction
        model = train_ml_model('AAPL')
        prediction = make_prediction(model, ticker, data)
        print("Prediction:", "BUY" if prediction[0] == 1 else "SELL")
        return JsonResponse({'prediction': prediction[0]})

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='predict'),
]
