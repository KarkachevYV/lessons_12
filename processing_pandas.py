import pandas as pd

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
df = pd.read_csv('World-happiness-report-2024.csv')
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
print(df.loc[56])
print(df.loc[56, 'Perceptions of corruption'])
# 8 этап конкретизируем выборку через условие
print(df[df['Healthy life expectancy'] > 0.7])