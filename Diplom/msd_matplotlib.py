import matplotlib.pyplot as plt


months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
sales = [200, 180, 220, 260, 300, 320, 340, 310, 300, 290, 270, 250]


plt.plot(months, sales)
plt.title('Monthly Sales Data - Matplotlib')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.grid(True)
plt.show()
