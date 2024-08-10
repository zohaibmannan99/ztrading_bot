import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from zbot.models import FinancialData

def prepare_data(ticker):
    data = FinancialData.objects.filter(ticker=ticker).order_by('date')
    data = list(data)
    
    # Feature Engineering (example: using moving averages)
    features = []
    labels = []
    for i in range(100, len(data)):
        short_ma = np.mean([d.close for d in data[i-40:i]])
        long_ma = np.mean([d.close for d in data[i-100:i]])
        
        features.append([short_ma, long_ma])
        labels.append(1 if short_ma > long_ma else 0)  # 1 for 'BUY', 0 for 'SELL'

    return np.array(features), np.array(labels)

def train_ml_model(ticker):
    X, y = prepare_data(ticker)
    
    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize and train the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f'Model Accuracy: {accuracy * 100:.2f}%')
    
    return model

def make_prediction(model, ticker, data):
    X, _ = prepare_data(ticker)
    return model.predict(X[-1].reshape(1, -1))  # Predict for the most recent data point
