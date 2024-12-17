import pandas as pd
import plotly.express as px

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
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Производитель', value_name='Продажи')

# Суммирование продаж по производителям
vendor_sales = monthly_data_melted.groupby('Производитель')['Продажи'].sum().reset_index()

# Построение круговой диаграммы с помощью Plotly
fig = px.pie(vendor_sales, values='Продажи', names='Производитель', title='Доля продаж по производителям')

# Отображение графика
fig.show()
