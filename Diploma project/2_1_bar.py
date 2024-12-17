import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загрузка данных из CSV
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
df = pd.read_csv(file_path)

# Установка индекса по дате
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(12,6))

# Настройка параметров для многорядной столбчатой диаграммы
bar_width = 0.2
x = np.arange(len(df))  # Позиции по оси x для месяцев

# Построение столбцов для каждой марки
plt.bar(x - bar_width, df['Apple'], width=bar_width, label='Apple')
plt.bar(x, df['Samsung'], width=bar_width, label='Samsung')
plt.bar(x + bar_width, df['Xiaomi'], width=bar_width, label='Xiaomi')
plt.bar(x + 2 * bar_width, df['Other'], width=bar_width, label='Other')

# Настройка графика
plt.xlabel('Месяц')
plt.ylabel('Доля (%)')
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xticks(x, df.index.strftime('%Y-%m'), rotation=45)  # Форматирование меток по оси x
plt.legend()  # Отображение легенды

# Отображение графика
plt.tight_layout()
plt.show()
