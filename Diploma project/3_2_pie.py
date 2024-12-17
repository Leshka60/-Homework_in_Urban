import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразование столбца 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Установка 'Date' в качестве индекса
data.set_index('Date', inplace=True)

# Группировка данных по месяцу и суммирование значений
monthly_data = data.resample('ME').sum().reset_index()

# Преобразование данных в длинный формат для анализа
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Суммирование продаж по производителям
vendor_sales = monthly_data_melted.groupby('Vendor')['Sales'].sum()

# Настройка стиля Seaborn
sns.set(style="whitegrid")

# Построение круговой диаграммы
plt.figure(figsize=(10, 7))
plt.pie(vendor_sales, labels=vendor_sales.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette("pastel"))
plt.title('Доля продаж по производителям')
plt.axis('equal')  # Чтобы круговая диаграмма выглядела как круг

# Отображение графика
plt.show()
