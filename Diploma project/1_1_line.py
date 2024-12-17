import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Устанавливаем 'Date' как индекс
data.set_index('Date', inplace=True)

# Построение графика
plt.figure(figsize=(12, 6))

# Строим линии для каждой операционной системы
plt.plot(data.index, data['Apple'], label='Apple', marker='o')
plt.plot(data.index, data['Samsung'], label='Samsung', marker='o')
plt.plot(data.index, data['Xiaomi'], label='Xiaomi', marker='o')
plt.plot(data.index, data['Other'], label='Other', marker='o')

# Добавление заголовка и меток осей
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xlabel('Дата')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Отображение графика
plt.tight_layout()
plt.show()
