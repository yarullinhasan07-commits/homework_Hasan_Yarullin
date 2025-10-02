import numpy as np
import matplotlib.pyplot as plt
x = ['Янв', 'Фев', 'Март', 'Апр', 'Май', 'Июнь', 'Июль', 'Авг', 'Сент', 'Окт', 'Нояб', 'Дек']
y = [-12, -7, 3, 10, 18, 23, 25, 22, 16, 9, 1, -6]
plt.bar(x, y, label='По данным Московского метеоцентра', alpha=0.5 )
plt.plot(x, y, color='blue', marker='o', markersize=6)
plt.xlabel('Месяц года')
plt.ylabel('Температура в градусах')
plt.title('Среднемесячные температуры')
plt.legend(loc='best')
plt.show()