import pandas as pd
import plotly.graph_objects as go

# Загрузка данных из CSV файла
file_path = 'https://raw.githubusercontent.com/Leshka60/-Homework_in_Urban/main/Diploma%20project/vendor-ww-monthly.csv'
data = pd.read_csv(file_path)

# Преобразуем столбец 'Date' в формат datetime
data['Date'] = pd.to_datetime(data['Date'])

# Создаем график
fig = go.Figure()

# Добавляем линии для каждого производителя
fig.add_trace(go.Scatter(x=data['Date'], y=data['Apple'], mode='lines+markers', name='Apple'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Samsung'], mode='lines+markers', name='Samsung'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Xiaomi'], mode='lines+markers', name='Xiaomi'))
fig.add_trace(go.Scatter(x=data['Date'], y=data['Other'], mode='lines+markers', name='Other'))

# Настройка заголовка и меток осей
fig.update_layout(
    title='Доля производителей смартфонов с июня 2024 по ноябрь 2024',
    xaxis_title='Дата',
    yaxis_title='Доля (%)',
    legend_title='Производители',
    xaxis=dict(tickformat='%Y-%m-%d'),
    template='plotly_white'
)

# Отображение графика
fig.show()
