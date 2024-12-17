import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Устанавливаем 'Date' как индекс
data.set_index('Date', inplace=True)

# Сброс индекса для использования в Seaborn
data_reset = data.reset_index()

# Построение линейного графика с использованием Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(data=data_reset, x='Date', y='Apple', label='Apple', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Samsung', label='Samsung', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Xiaomi', label='Xiaomi', marker='o')
sns.lineplot(data=data_reset, x='Date', y='Other', label='Other', marker='o')

# Добавление заголовка и меток осей
plt.title('Доля производителей с июня 2024 по ноябрь 2024')
plt.xlabel('Дата')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend()
plt.grid()

# Отображение графика
plt.tight_layout()
plt.show()