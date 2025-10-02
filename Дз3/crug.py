import numpy as np
import matplotlib.pyplot as plt
amount = [5, 16 , 39, 12, 28]
groups = ["Мое свободное время", "Вромя когда я кушаю", "То время когда книшки читаю", "Вот столько я сплю", "Футбол смотрю"]
colors = plt.cm.viridis(np.linspace(0, 1100, len(amount)))
plt.pie(amount, labels=groups, autopct='%1.f%%')
plt.title("Как я провожу свое время")
plt.show()