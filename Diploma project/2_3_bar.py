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

# Преобразование данных в длинный формат для Plotly
monthly_data_melted = monthly_data.melt(id_vars='Date', var_name='Vendor', value_name='Sales')

# Построение столбчатой диаграммы
fig = px.bar(monthly_data_melted, x='Date', y='Sales', color='Vendor',
             title='Доля производителей смартфонов с июня 2024 по ноябрь 2024',
             labels={'Sales': 'Доля (%)', 'Date': 'Месяц', 'Vendor': 'Производитель'},
             text='Sales')

# Настройка отображения значений на столбцах
fig.update_traces(texttemplate='%{text:.2s}', textposition='outside')

# Отображение графика
fig.show()
