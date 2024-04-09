import pandas as pd

def calculate_and_display_average_price(data):

    if 'Close' not in data.columns:
        print("Столбец 'Close' отсутствует в DataFrame.")
        return

    average_price = data['Close'].mean()

    print("Средняя цена закрытия за заданный период:", average_price)

data = pd.DataFrame({
    'Date': ['2024-04-01', '2024-04-02', '2024-04-03'],
    'Close': [100, 110, 120]
})

calculate_and_display_average_price(data)
