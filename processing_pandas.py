import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("kanchana1990/world-internet-usage-data-2023-updated")

print("Path to dataset files:", path)
# 1 этап - пример использования series
# data = [1, 2, 3, 4, 5]
# series = pd.Series(data)
# print(series)

# 2 этап - пример использования Data Frame
# data = {
#   'Name' : ['Alice', 'Bob', 'Roma', 'Anna'],
#   'Age' : [23, 45, 17, 24],
#   'City' : ['New York', 'LA', 'Chicago', 'Moscow']
# }

# df = pd.DataFrame(data)
# print(df)

# 3 этап вывод первых пять строк со встроенной функцией  head() и последних с помощью вст. функцией tail()
#df = pd.read_csv('World-happiness-report-2024.csv')
# print(df.head())
# print(df.tail())
# 4 этап выводим базовую информацию о дата фрейме
#print(df.info())
# 5 этап выводим статистическую информацию о дата фрейме
#print(df.describe())
# 6 этап выводим кокретную информацию о дата фрейм
# df.columns = df.columns.str.strip()
# print(df.columns)
# print(df[['Country name', 'Regional indicator']])
# 7 этап выводим конкретную строчку дата фрейма или только какой нибудь показатель из сточки
#print(df.loc[56])
#print(df.loc[56, 'Perceptions of corruption'])
# 8 этап конкретизируем выборку через условие
#print(df[df['Healthy life expectancy'] > 0.7])
# 9 этап редактирование дата фрейма
# добавление столбца
#df = pd.read_csv('hh.csv')
#df['Test'] = [new for new in range(29)]
#print(df)
# удаление столбца(строки) с конкретным названием, axis=1(столбец и 0-строка), с изменением исходного состояния приinplace=True (False - без изменения).
#df.drop('Test', axis=1, inplace=True)
#df.drop(28, axis=0, inplace=True)
#print(df)
# 10 этап работа с неполными(частично не заполненными) дата сетами
#df = pd.read_csv('animal.csv')
# print(df)
#df.fillna(0, inplace=True) # вариант вставки значений = 0
# print(df)
# df.dropna(inplace=True) #вариант удаления не желательный,
# print(df)
#выборка по группам
#group = df.groupby('Пища')['Средняя продолжительность жизни'].mean()
#print(group)
# для сохранения любого дата сета
#df.to_csv('newanimal.csv')
df = pd.read_csv('internet_users.csv')
print(df.head())
print(df.info())
print(df.describe())