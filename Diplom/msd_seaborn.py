import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 180, 220, 260, 300, 320, 340, 310, 300, 290, 270, 250]


data = pd.DataFrame({'Month': months, 'Sales': sales})

# Использование другой цветовой палитры
sns.set_palette("husl")
sns.lineplot(x='Month', y='Sales', data=data, marker='o')  # Adding markers for each data point

plt.title('Monthly Sales Data - Seaborn')
plt.xlabel('Month')
plt.ylabel('Sales')

# Добавление меток точек данных
for i, faa in enumerate(sales):
    plt.text(months[i], sales[i], f'{faa}', ha='center', va='bottom')

plt.grid(True)
plt.show()
