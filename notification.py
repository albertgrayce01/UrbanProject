def notify_if_strong_fluctuations(data, threshold):
    max_price = max(data)
    min_price = min(data)
    price_range = max_price - min_price
    fluctuation_percentage = (price_range / min_price) * 100
    if fluctuation_percentage > threshold:
        print("Strong fluctuations detected! Price range exceeded threshold of {}%".format(threshold))
    else:
        print("Fluctuations are within threshold.")
stock_prices = [100, 105, 95, 110, 90, 115, 120]
threshold = 10
notify_if_strong_fluctuations(stock_prices, threshold)
