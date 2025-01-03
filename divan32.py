import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
x = np.random.rand(5)  # массив из 5 случайных чисел для оси X
y = np.random.rand(5)  # массив из 5 случайных чисел для оси Y

# Печать массива случайных чисел
print("Массив X:", x)
print("Массив Y:", y)

# Построение диаграммы рассеяния
plt.scatter(x, y)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния случайных данных')
plt.xlabel('Случайные данные X')
plt.ylabel('Случайные данные Y')

# Показать график
plt.show()