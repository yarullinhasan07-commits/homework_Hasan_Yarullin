import numpy as np
import matplotlib.pyplot as plt
x = [10, 12, 24, 54, 75, 89, 106, 136, 159, 183]
y = [1, 1.1, 2, 5, 6.8, 15, 24, 36, 55, 98]
plt.plot(x, y, color='green', marker='o')
plt.xlabel('Рост') 
plt.ylabel('Вес') 
plt.title('Зависимость веса человека от роста') 
plt.grid(True)
plt.show()