import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразование столбца 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Установка 'Date' в качестве индекса
data.set_index('Date', inplace=True)

# Группировка данных по месяцу и суммирование значений
monthly_data = data.resample('ME').sum().reset_index()

# Настройка стиля Seaborn
sns.set(style="darkgrid")

sns.set_palette("husl")

# Преобразование данных в длинный формат для Seaborn
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Построение столбчатой диаграммы
plt.figure(figsize=(12, 6))
sns.barplot(data=monthly_data_melted, x='Date', y='Sales', hue='Vendor')

# Настройка заголовка и меток осей
plt.title('Доля производителей смартфонов с июня 2024 по ноябрь 2024')
plt.xlabel('Месяц')
plt.ylabel('Доля (%)')
plt.xticks(rotation=45)
plt.legend(title='Производители')

# Отображение графика
plt.tight_layout()
plt.show()
