import plotly.express as px
import pandas as pd


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 180, 220, 260, 300, 320, 340, 310, 300, 290, 270, 250]

data = pd.DataFrame({'Month': months, 'Sales': sales})

# Использование Plotly для построения интерактивной диаграммы
fig = px.line(data, x='Month', y='Sales', title='Monthly Sales Data - Plotly',
              line_shape='linear', markers=True, color_discrete_sequence=['fuchsia'])

# Настройка демонстрации данных при наведении курсора мыши
fig.update_traces(text=sales, hoverinfo='text+x+y')

fig.update_xaxes(title_text='Month')
fig.update_yaxes(title_text='Sales')
fig.show()
