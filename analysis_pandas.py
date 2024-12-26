import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

#   ввод в описательную статистику
# data = {
#     'Набор А': [85, 90, 95, 100, 105],
#     'Набор Б': [70, 80, 95, 110, 120],
# }

# df = pd.DataFrame(data)

# stdA = df['Набор А'].std()
# stdB = df['Набор Б'].std()


# print(f"Стандартное отклонение 1 набор - {stdA}")
# print(f"Стандартное отклонение 2 набор - {stdB}")

# статистический анализ тематческого набора
# data = {
#     'Возраст': [23, 22, 21, 27, 23, 20, 29, 28, 22, 25],
#     'Зарплата': [54000, 58000, 60000, 52000, 55000, 59000, 51000, 49000, 53000, 61000],
# }

# df = pd.DataFrame(data)

# # вывод полной статстической информации дата сета
# print(df.describe())

# # вывод статстической информации дата сета по отдельности:

# print(f"Средний возраст - {df['Возраст'].mean()}")
# print(f"Медианный возраст - {df['Возраст'].median()}")
# print(f"Стандартное отклонение возраста - {df['Возраст'].std()}")

# print(f"Средняя зарплата - {df['Зарплата'].mean()}")
# print(f"Медианная зп - {df['Зарплата'].median()}")
# print(f"Стандартное отклонение зп - {df['Зарплата'].std()}")

# статистический анализ временных рядов
# dates = pd.date_range(start='2022-07-26', periods=10, freq='D')
# values = np.random.rand(10)
# df = pd.DataFrame({'Date': dates, 'Value': values})
# df.set_index('Date', inplace=True)

# print(df)

# month = df.resample('ME').mean()
# print(month)

# data = {'value': [1, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 55]}
# df = pd.DataFrame(data)

# # # построим гистограмму для визуализации распределения данных, чтобы понять их поведение, выявить закономерности и аномалии.
# # df['value'].hist()
# # plt.show()

# # # построим коробчатую диаграмму для визуализации распределения числовых данных. 
# # df.boxplot(column='value')
# # plt.show()
# #использование встроенной функции describe() выдаёт квартили
# #print(df.describe())
# Q1 = df['value'].quantile(0.25)
# Q3 = df['value'].quantile(0.75)

# IQR = Q3 - Q1
# # необходимые для определения границ межквартального размаха
# downside = Q1 - 1.5 * IQR
# upside = Q3 + 1.5 * IQR
# # что в свою очередь используется для удаления выбросов
# # удаление производится  через условия , для чего создаётся новый дата сет
# df_new = df[(df['value'] >= downside) & (df['value'] <= upside)]
# df_new.boxplot(column='value')
# plt.show()

#выберём тематический набор
# data = {
#     'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
#     'gender': ['female', 'male', 'male', 'male', 'female'],
#     'department': ['HR', 'Engineering', 'Marketing', 'Engineering', 'HR']
# }
# df = pd.DataFrame(data)
# # Преобразуем столбцы в категориальные данные
# df['gender'] = df['gender'].astype('category')
# df['department'] = df['department'].astype('category')

# # анализируем варианты выбора
# print(df['gender'].cat.categories)
# print(df['department'].cat.categories)

# # и их числовые коды
# print(df['gender'].cat.codes)

# # добавление новых категорий производится следующим кодом
# df['department'] = df['department'].cat.add_categories(['Finance'])

# # удаление следующим
# df['department'] = df['department'].cat.remove_categories(['HR'])
# print(df['department'].cat.categories)
students_grades = {
    "Ученик 1": {"Математика": 4, "Физика": 3, "Химия": 5, "Литература": 3, "История": 4},
    "Ученик 2": {"Математика": 5, "Физика": 4, "Химия": 4, "Литература": 4, "История": 5},
    "Ученик 3": {"Математика": 3, "Физика": 4, "Химия": 3, "Литература": 4, "История": 3},
    "Ученик 4": {"Математика": 5, "Физика": 5, "Химия": 5, "Литература": 5, "История": 5},
    "Ученик 5": {"Математика": 2, "Физика": 3, "Химия": 2, "Литература": 4, "История": 3},
    "Ученик 6": {"Математика": 4, "Физика": 4, "Химия": 4, "Литература": 4, "История": 4},
    "Ученик 7": {"Математика": 5, "Физика": 5, "Химия": 5, "Литература": 5, "История": 5},
    "Ученик 8": {"Математика": 3, "Физика": 3, "Химия": 3, "Литература": 3, "История": 2},
    "Ученик 9": {"Математика": 5, "Физика": 5, "Химия": 5, "Литература": 5, "История": 5},
    "Ученик 10": {"Математика": 4, "Физика": 4, "Химия": 4, "Литература": 4, "История": 4},
}
#выводим первые пять строк
df = pd.DataFrame(students_grades)
print(df)
# Создаём DataFrame
df = pd.DataFrame(students_grades).T

# Вычисляем средние оценки
average_grades = df.mean()

# Вычисляем медианные оценки
median_grades = df.median()

# Выводим результаты
print("Средние оценки по предметам:")
print(average_grades)
print("\nМедианные оценки по предметам:")
print(median_grades)

# Извлекаем оценки по математике
math_grades = [4, 5, 3, 5, 2, 4, 5, 3, 5, 4]

# Вычисляем первый и третий квартиль
Q1 = np.quantile(math_grades, 0.25)
Q3 = np.quantile(math_grades, 0.75)

# Вычисляем межквартильный размах
IQR = Q3 - Q1

# Определяем границы
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"\nПервый квартиль (Q1): {Q1}")
print(f"Третий квартиль (Q3): {Q3}")
print(f"Межквартильный размах (IQR): {IQR}")
print(f"Нижняя граница: {lower_bound}")
print(f"Верхняя граница: {upper_bound}\n")

subjects = ["Математика", "Физика", "Химия", "Литература", "История"]

# Вычисляем стандартное отклонение для каждого предмета
for subject in subjects:
    grades = [grades[subject] for grades in students_grades.values()]
    std_dev = np.std(grades, ddof=0)  # Используем ddof=0 для выборки всей совокупности
    print(f"Стандартное отклонение по предмету {subject}: {std_dev:.2f}")

# Собираем все оценки в один список
grades = []
for student, subjects in students_grades.items():
    grades.extend(subjects.values())

# Вычисляем стандартное отклонение
std_deviation = np.std(grades)

print(f"\nСтандартное отклонение оценок: {std_deviation:.2f}")