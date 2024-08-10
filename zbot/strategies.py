from zbot.models import FinancialData

def moving_average_crossover(ticker, short_window=40, long_window=100):
    # Fetch the data for the given ticker
    data = FinancialData.objects.filter(ticker=ticker).order_by('date')
    
    # Ensure enough data is available
    if data.count() < long_window:
        return None
    
    data = list(data)

    # Calculate moving averages
    short_ma = [sum([d.close for d in data[i-short_window:i]]) / short_window for i in range(short_window, len(data))]
    long_ma = [sum([d.close for d in data[i-long_window:i]]) / long_window for i in range(long_window, len(data))]

    signals = []
    for i in range(len(long_ma)):  # Align loop with long_ma
        if short_ma[i + (long_window - short_window)] > long_ma[i]:
            signals.append(('BUY', data[i + long_window].date))
        elif short_ma[i + (long_window - short_window)] < long_ma[i]:
            signals.append(('SELL', data[i + long_window].date))
    
    return signals


def backtest_strategy(strategy, ticker):
    signals = strategy(ticker)
    
    if signals is None:
        print("Not enough data to backtest.")
        return
    
    print(f"Backtesting {strategy.__name__} on {ticker}")
    for signal in signals:
        print(f"{signal[0]} on {signal[1]}")
